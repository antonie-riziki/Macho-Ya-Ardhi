from flask import Flask, request
import sys
import os

# Ensure local imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from send_sms import chunk_message
from ai_response import (
    land_risk_analysis_func,
    land_buying_tips_func,
    fraud_reporting_guidance_func,
    facility_locator_func,
)

app = Flask(__name__)

@app.route("/ussd", methods=["POST"])
def ussd():
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "")

    parts = text.split("*")
    level = len(parts) if text else 0

    # ----------------------------- #
    # MAIN MENU
    # ----------------------------- #
    if text == "":
        response = "CON Welcome to Mradi wa Ardhi\n"
        response += "1. Check Parcel Risk\n"
        response += "2. Land Buying Tips\n"
        response += "3. Find Land Registry\n"
        response += "4. Report Fraud / Help\n"

    # ----------------------------- #
    # SECTION 1: CHECK PARCEL RISK
    # ----------------------------- #
    elif parts[0] == "1":
        if level == 1:
            response = "CON Enter Parcel Number (e.g. NBI/BLOCK12/34):"
        elif level == 2:
            parcel_no = parts[1]
            analysis = land_risk_analysis_func(parcel_no)
            response = f"END {chunk_message(phone_number, analysis)}"

    # ----------------------------- #
    # SECTION 2: LAND BUYING TIPS
    # ----------------------------- #
    elif parts[0] == "2":
        tips = land_buying_tips_func()
        response = f"END {chunk_message(phone_number, tips)}"

    # ----------------------------- #
    # SECTION 3: LAND REGISTRY LOCATOR
    # ----------------------------- #
    elif parts[0] == "3":
        registries = facility_locator_func()
        response = f"END {chunk_message(phone_number, registries)}"

    # ----------------------------- #
    # SECTION 4: REPORT FRAUD / HELP
    # ----------------------------- #
    elif parts[0] == "4":
        if level == 1:
            response = "CON Fraud & Emergency Help\n"
            response += "1. How to Report Fraud\n"
            response += "2. DCI Land Fraud Hotline\n"
        elif level == 2:
            if parts[1] == "1":
                guidance = fraud_reporting_guidance_func()
                response = f"END {chunk_message(phone_number, guidance)}"
            elif parts[1] == "2":
                response = "END Please call 020-2711611 (DCI) or visit the nearest police station."

    # ----------------------------- #
    # DEFAULT FALLBACK
    # ----------------------------- #
    else:
        response = "END Invalid input. Try again."

    return response

if __name__ == "__main__":
    app.run(debug=True, port=8001)
