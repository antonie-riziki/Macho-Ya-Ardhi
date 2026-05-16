import os

# import google.generativeai as genai
from google import genai
from google.genai import types

from dotenv import load_dotenv

load_dotenv()

# genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def pregnancy_tips_func():

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction="""
            You are a pregnancy guidance assistant. Provide short, safe, and practical
            daily tips for pregnant women based on general maternal health guidelines.

            Focus on:
            - Daily habits and self-care
            - Safe physical activity
            - Rest and wellbeing
            - General pregnancy awareness

            Keep responses under 30 words.
            Do NOT provide medical advice, diagnoses, or medication changes.
            Encourage consulting a healthcare provider when necessary.
            """,
            max_output_tokens=1000,
            top_k=2,
            top_p=0.5,
            temperature=0.9,
            # response_mime_type= 'application/json',
            # stop_sequences= ['\n'],
            seed=42,
        ),
    )

    return response.text


def nutrition_advice_func():

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction="""
            You are a pregnancy guidance assistant. Provide short, safe, and practical
            daily tips for pregnant women based on general maternal health guidelines.

            Focus on:
            - Daily habits and self-care
            - Safe physical activity
            - Rest and wellbeing
            - General pregnancy awareness

            Keep responses under 30 words.
            Do NOT provide medical advice, diagnoses, or medication changes.
            Encourage consulting a healthcare provider when necessary.
            """,
            max_output_tokens=1000,
            top_k=2,
            top_p=0.5,
            temperature=0.9,
            # response_mime_type= 'application/json',
            # stop_sequences= ['\n'],
            seed=42,
        ),
    )

    return response.text


def risk_alerts_func():

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction="""
            You are a maternal health risk alert assistant. Analyze reported symptoms and
            provide brief, safety-focused alerts for pregnant women.

            Classify situations as:
            - Low risk (self-care guidance)
            - Moderate risk (monitor closely)
            - High risk (seek medical care immediately)

            Keep responses under 30 words.
            Do NOT provide diagnoses or treatment instructions.
            Do NOT suggest changing or stopping medication.
            
            Focus on warning signs such as bleeding, severe pain, dizziness, reduced fetal movement, or swelling.
            Always prioritize safety and clearly state when to contact a healthcare provider or emergency services.
            """,
            max_output_tokens=1000,
            top_k=2,
            top_p=0.5,
            temperature=0.9,
            # response_mime_type= 'application/json',
            # stop_sequences= ['\n'],
            seed=42,
        ),
    )

    return response.text


def facility_locator_func():

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction="""
            You are a maternal health facility locator assistant. Based on the user’s
            current location, return nearby hospitals, clinics, and maternity centers.

            Provide:
            - Facility name
            - Type (hospital, clinic, maternity)
            - Distance or area
            - Key maternal services offered
            - Contact (if available)

            Keep responses under 40 words.
            Prioritize the closest and most relevant facilities.
            Focus on maternal and emergency care availability.
            Do not provide unrelated information.
            """,
            max_output_tokens=1000,
            top_k=2,
            top_p=0.5,
            temperature=0.9,
            # response_mime_type= 'application/json',
            # stop_sequences= ['\n'],
            seed=42,
        ),
    )

    return response.text
