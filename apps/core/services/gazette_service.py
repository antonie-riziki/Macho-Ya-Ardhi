import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "gazette_mock.json"


def search_gazette(parcel_number: str):
    if not DATA_FILE.exists():
        return []
    records = json.loads(DATA_FILE.read_text())
    if not parcel_number:
        return []
    normalized = parcel_number.lower().strip()
    exact = [r for r in records if r.get("parcel_number", "").lower() == normalized]
    if exact:
        return exact
    return [r for r in records if normalized in r.get("parcel_number", "").lower()]
