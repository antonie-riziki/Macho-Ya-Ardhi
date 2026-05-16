import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def land_risk_analysis_func(parcel_number):
    """Analyzes risk for a specific parcel number."""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction="""
            You are Mradi wa Ardhi, a land transaction risk agent in Kenya.
            Analyze the risk for the provided parcel number.
            Provide a short, critical assessment of potential red flags:
            - Overlapping titles
            - Gazette revocation history (simulated)
            - Seller verification tips.
            Keep response under 40 words.
            """,
            max_output_tokens=150,
        ),
        contents=f"Analyze risk for parcel: {parcel_number}"
    )
    return response.text

def land_buying_tips_func():
    """Provides general safe land buying tips."""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction="""
            Provide 3 high-impact, short tips for safe land transactions in Kenya.
            Focus on Search, LCB Consent, and Surveyor verification.
            Keep response under 30 words.
            """,
        ),
        contents="Safe land buying tips"
    )
    return response.text

def fraud_reporting_guidance_func():
    """Provides guidance on how to report land fraud."""
    return "To report fraud: 1. File a report with DCI Land Fraud Unit. 2. Contact the Land Registrar. 3. Engage a lawyer to place a caveat."

def facility_locator_func():
    """Locates nearest Land Registries (simplified)."""
    return "Nearest Land Registries: 1. Ardhi House (Nairobi) 2. Mombasa Registry 3. Kisumu Registry. Use 'Find on Map' in the web app for more."
