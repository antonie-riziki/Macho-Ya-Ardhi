def generate_report(metadata, extracted_documents, inconsistencies, gazette_matches, risk):
    report = {
        "transaction_summary": metadata,
        "extracted_documents": extracted_documents,
        "inconsistencies": inconsistencies,
        "gazette_matches": gazette_matches,
        "risk_score": risk["score"],
        "risk_level": risk["level"],
        "recommendations": risk["recommendations"],
        "final_verdict": "HIGH FRAUD RISK" if risk["level"] == "HIGH" else "PROCEED WITH CAUTION",
    }
    md = [
        "# Macho Ya Ardhi Risk Report",
        f"- **Risk Level:** {risk['level']}",
        f"- **Risk Score:** {risk['score']}",
        "## Inconsistencies",
    ] + [f"- {x}" for x in inconsistencies or ["No major inconsistencies found."]]
    if gazette_matches:
        md += ["## Gazette Matches"] + [f"- {m['parcel_number']}: {m['issue']} ({m['notice_date']})" for m in gazette_matches]
    md += ["## Recommendations"] + [f"- {r}" for r in risk["recommendations"]]
    return report, "\n".join(md)
