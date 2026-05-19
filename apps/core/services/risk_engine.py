
def compute_risk(extracted_documents, gazette_matches):
    score = 0
    findings = []

    parcels = {d.get("parcel_number") for d in extracted_documents if d.get("parcel_number")}
    owners = {d.get("registered_owner") for d in extracted_documents if d.get("registered_owner")}
    sellers = {d.get("seller_name") for d in extracted_documents if d.get("seller_name")}

    if len(parcels) > 1:
        score += 40; findings.append("Parcel mismatch across documents")
    if len(owners) > 1:
        score += 30; findings.append("Registered owner mismatch")
    if len(sellers) > 1:
        score += 20; findings.append("Seller mismatch")

    for doc in extracted_documents:
        if not doc.get("stamp_present", False):
            score += 20; findings.append(f"Missing stamp in {doc.get('document_type','document')}")
        if not doc.get("signature_present", False):
            score += 15; findings.append(f"Missing signature in {doc.get('document_type','document')}")
        if doc.get("suspicious_edits"):
            score += 35; findings.append("Suspicious edits/tampering detected")
        if not doc.get("parcel_number"):
            score += 25; findings.append("Missing parcel number")
        if float(doc.get("confidence", 0)) < 0.6:
            score += 10; findings.append("Low Gemini extraction confidence")

    if gazette_matches:
        score += 50
        findings.append("Parcel appears in Kenya Gazette dispute/loss records")

    level = "LOW" if score <= 20 else "MEDIUM" if score <= 50 else "HIGH"
    recs = ["Run official land registry search (Ardhisasa/manual search).", "Engage a property lawyer before payment."]
    if level == "HIGH":
        recs.insert(0, "Do NOT proceed with transaction until discrepancies are resolved.")
    return {"score": score, "level": level, "findings": findings, "recommendations": recs}
