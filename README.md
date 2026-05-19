# Macho Ya Ardhi (Django MVP)

Kenyan land transaction fraud detection demo with Gemini Vision extraction + Gazette mock cross-check + risk scoring.

## Required environment variables
- `GEMINI_API_KEY`
- `GOOGLE_CLOUD_PROJECT`
- `GOOGLE_APPLICATION_CREDENTIALS`
- `VERTEX_AI_LOCATION`
- `SECRET_KEY`
- `DEBUG`

## Quickstart
```bash
pip install -r requirements.txt
cd MYA
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Demo flow
1. Upload one or more land document images/PDFs.
2. Optionally fill parcel number/county/seller.
3. Submit to `POST /api/verify-land/`.
4. Review risk output and markdown report in the UI.
5. Fetch saved report with `GET /api/report/<id>/`.

## Sample disputed parcel numbers
- `KJD/Kaputiei/1234`
- `Nairobi/Block/82/733`
- `LR/209/2489`

## Fallback behavior
- If Gemini key/credentials are missing or Gemini output is invalid, app uses safe mock extraction.
- If files are missing, API returns `400`.
- If file size is too large (>10MB), the document is flagged suspicious in demo mode.

## Google Cloud deployment (Cloud Run)
```bash
gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/macho-ya-ardhi

gcloud run deploy macho-ya-ardhi \
  --image gcr.io/$GOOGLE_CLOUD_PROJECT/macho-ya-ardhi \
  --platform managed \
  --region $VERTEX_AI_LOCATION \
  --allow-unauthenticated \
  --set-env-vars SECRET_KEY=$SECRET_KEY,DEBUG=False,GEMINI_API_KEY=$GEMINI_API_KEY,GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT,GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS,VERTEX_AI_LOCATION=$VERTEX_AI_LOCATION
```
