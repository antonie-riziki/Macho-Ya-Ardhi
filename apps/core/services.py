import os
from google import genai
from google.genai import types
from django.conf import settings

class LandRiskService:
    def __init__(self):
        self.api_key = getattr(settings, 'GOOGLE_API_KEY', os.getenv("GOOGLE_API_KEY"))
        self.client = genai.Client(api_key=self.api_key)

    def analyze_parcel_risk(self, parcel_number):
        """
        Analyzes the risk of a land parcel using AI.
        In a real scenario, this would also query the Kenya Gazette or Land Registry.
        """
        prompt = f"Analyze the land transaction risk for parcel number {parcel_number} in Kenya."
        
        try:
            response = self.client.models.generate_content(
                model="gemini-3-flash-preview",
                config=types.GenerateContentConfig(
                    system_instruction="""
                    You are a Land Transaction Risk Agent for Kenya. 
                    Provide a brief risk assessment for the given parcel number.
                    Focus on:
                    - Potential for overlapping titles
                    - Common fraud patterns in that area (if area can be inferred)
                    - General advice for the buyer.
                    Keep the response under 50 words.
                    """,
                    max_output_tokens=150,
                ),
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error analyzing risk: {str(e)}"

    def get_buying_tips(self):
        """Returns general safe land-buying tips."""
        try:
            response = self.client.models.generate_content(
                model="gemini-3-flash-preview",
                config=types.GenerateContentConfig(
                    system_instruction="""
                    You are a Land Transaction Advisor in Kenya.
                    Provide 3 short, high-impact tips for a safe land purchase.
                    Focus on verification steps like LCB consent and title search.
                    Keep it under 40 words.
                    """,
                ),
                contents="Give me safe land buying tips."
            )
            return response.text
        except Exception as e:
            return "1. Always do a title search. 2. Verify with Land Control Board. 3. Use a registered surveyor."

class SMSService:
    @staticmethod
    def send_sms(phone_number, message):
        """
        Simulates sending an SMS. 
        In production, integrate with Africa's Talking or Twilio.
        """
        print(f"SMS to {phone_number}: {message}")
        return True

    @staticmethod
    def chunk_message(phone_number, message):
        """Chunks long messages if needed (legacy helper)."""
        SMSService.send_sms(phone_number, message)
        return "(Sent via SMS)"
