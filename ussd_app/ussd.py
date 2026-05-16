from flask import Flask, request
import sys

sys.path.insert(1, "/")

from send_sms import chunk_message
from ai_response import (
    pregnancy_tips_func,
    risk_alerts_func,
    nutrition_advice_func,
    facility_locator_func,
)

app = Flask(__name__)


@app.route("/ussd", methods=["POST"])
def ussd():
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "")

    user_response = text.split("*")

    # ----------------------------- #
    # MAIN MENU
    # ----------------------------- #
    if text == "":
        response = "CON Welcome to InfaNest \n"
        response += "1. Daily Health Check\n"
        response += "2. Pregnancy Guidance\n"
        response += "3. Find Health Facility\n"
        response += "4. Emergency Help\n"

    # ----------------------------- #
    # SECTION 1: DAILY HEALTH CHECK
    # ----------------------------- #
    elif text == "1":
        response = "CON How are you feeling today?\n"
        response += "1. Good\n"
        response += "2. Okay\n"
        response += "3. Unwell\n"

    elif text == "1*1":
        response = "CON Any symptoms today?\n"
        response += "1. None\n"
        response += "2. Headache\n"
        response += "3. Bleeding\n"
        response += "4. Dizziness\n"

    elif text.startswith("1*1*"):
        response = f"END Thank you. Stay healthy. Tips sent shortly {chunk_message(phone_number, pregnancy_tips_func())}"

    elif text == "1*2":
        response = f"END Monitor your health closely. Tips sent shortly {chunk_message(phone_number, pregnancy_tips_func())}"

    elif text == "1*3":
        response = f"END Alert: Seek medical care immediately {chunk_message(phone_number, risk_alerts_func())}"

    # ----------------------------- #
    # SECTION 2: PREGNANCY GUIDANCE
    # ----------------------------- #
    elif text == "2":
        response = "CON Pregnancy Guidance\n"
        response += "1. Nutrition Tips\n"
        response += "2. Exercise Advice\n"
        response += "3. Medication Reminders\n"

    elif text == "2*1":
        response = f"END Nutrition tips sent {chunk_message(phone_number, nutrition_advice_func())}"

    elif text == "2*2":
        response = f"END Exercise guidance sent {chunk_message(phone_number, pregnancy_tips_func())}"

    elif text == "2*3":
        response = "END Remember to take your supplements daily (Iron, Folic Acid)"

    # ----------------------------- #
    # SECTION 3: FACILITY LOCATOR
    # ----------------------------- #
    elif text == "3":
        response = "CON Find Nearby Facility\n"
        response += "1. Nearest Hospital\n"
        response += "2. Maternity Clinics\n"

    elif text == "3*1":
        response = f"END Nearby hospitals sent via SMS {chunk_message(phone_number, facility_locator_func())}"

    elif text == "3*2":
        response = f"END Nearby maternity clinics sent via SMS {chunk_message(phone_number, facility_locator_func())}"

    # ----------------------------- #
    # SECTION 4: EMERGENCY HELP
    # ----------------------------- #
    elif text == "4":
        response = "CON Emergency Help\n"
        response += "1. Call Ambulance\n"
        response += "2. Find Emergency Facility\n"

    elif text == "4*1":
        response = "END Please call 999 or 112 immediately for emergency assistance"

    elif text == "4*2":
        response = f"END Emergency facilities sent {chunk_message(phone_number, facility_locator_func())}"

    # ----------------------------- #
    # DEFAULT FALLBACK
    # ----------------------------- #
    else:
        response = "END Invalid input. Try again."

    return response


if __name__ == "__main__":
    app.run(debug=True, port=8001)
