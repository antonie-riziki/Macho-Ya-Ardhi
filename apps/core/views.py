import json
import uuid

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods

from .models import LandParcel, TransactionCase
from .services.gazette_service import search_gazette
from .services.gemini_service import analyze_document
from .services.report_service import generate_report
from .services.risk_engine import compute_risk


def verify_page(request):
    return render(request, "verification.html")


@csrf_exempt
@require_http_methods(["POST"])
def verify_land(request):
    files = request.FILES.getlist("documents")
    if not files:
        return JsonResponse({"error": "Please upload at least one document."}, status=400)

    metadata = {
        "buyer_name": request.POST.get("buyer_name", ""),
        "seller_name": request.POST.get("seller_name", ""),
        "county": request.POST.get("county", ""),
        "parcel_number": request.POST.get("parcel_number", ""),
    }

    extracted_documents = []
    for f in files:
        if f.size > 10 * 1024 * 1024:
            extracted = {"document_type": f.name, "suspicious_edits": True, "confidence": 0.3, "parcel_number": ""}
        else:
            extracted = analyze_document(f)
        extracted["file_name"] = f.name
        extracted_documents.append(extracted)

    candidate_parcel = metadata["parcel_number"] or next((d.get("parcel_number") for d in extracted_documents if d.get("parcel_number")), "")
    gazette_matches = search_gazette(candidate_parcel)
    risk = compute_risk(extracted_documents, gazette_matches)
    report, markdown_report = generate_report(metadata, extracted_documents, risk["findings"], gazette_matches, risk)

    parcel_obj, _ = LandParcel.objects.get_or_create(
        parcel_number=candidate_parcel or f"UNKNOWN-{uuid.uuid4().hex[:8]}", defaults={"location": metadata.get("county") or "Unknown"}
    )
    case = TransactionCase.objects.create(parcel=parcel_obj, buyer_name=metadata.get("buyer_name") or "Demo Buyer", risk_score=risk["level"], summary=json.dumps(report))

    return JsonResponse({
        "report_id": case.id,
        "extracted_documents": extracted_documents,
        "risk": risk,
        "gazette_matches": gazette_matches,
        "markdown_report": markdown_report,
    })


@require_GET
def report_detail(request, report_id):
    try:
        case = TransactionCase.objects.get(id=report_id)
        report = json.loads(case.summary)
    except Exception:
        return JsonResponse({"error": "Report not found"}, status=404)
    return JsonResponse({"report_id": case.id, "report": report})
