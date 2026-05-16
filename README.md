# Mradi wa Ardhi — Land Transaction Risk Agent

# LIVE LIN: https://ai.studio/apps/6949e8da-aee6-4142-b104-eafb62d25ae9
## the previous repo was private Kindly use this one which is public

 *"Ardhi ni uhai"* — Land is life. In Kenya, it's also one of the most dangerous places to put your money.

**Mradi wa Ardhi** is an AI-powered land fraud detection agent for Kenya. Upload your land documents — title deeds, sale agreements, IDs, survey maps — and the agent stress-tests them for inconsistencies, forgery red flags, and public record conflicts before you sign a single page.

---

## The Problem

Buying land in Kenya can destroy a family financially. Fraudsters sell the same plot twice, forge title deeds, alter parcel numbers, backdate consent documents, and exploit the gaps between paper records and official registries.

A single transaction involves up to **10+ document types**: title deeds, parcel search certificates, sale agreements, Land Control Board consents, mutation forms, survey maps, rates clearance certificates, Kenya Gazette notices, seller ID, and KRA PIN certificates. Most buyers — and even some lawyers — review these documents manually, in isolation, without cross-checking them against each other or public records.

By the time fraud is discovered, the money is gone.

**Mradi wa Ardhi catches what human eyes miss** — before money changes hands.

---

## Agent Architecture

The system is built as a **multi-step AI agent pipeline** using Google ADK and Gemini Vision.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        USER / BUYER                                  │
│            Uploads document photos via web interface                │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   ORCHESTRATOR AGENT (Google ADK)                   │
│         Manages the transaction session and agent flow              │
└───┬──────────────────┬───────────────────┬──────────────────────────┘
    │                  │                   │
    ▼                  ▼                   ▼
┌──────────┐   ┌──────────────┐   ┌───────────────────┐
│ VISION   │   │ CONSISTENCY  │   │  GAZETTE SEARCH   │
│  AGENT   │   │   AGENT      │   │      AGENT        │
│          │   │              │   │                   │
│ Gemini   │   │ Cross-checks │   │ Searches Kenya    │
│ Vision   │   │ all docs for │   │ Gazette for lost  │
│ extracts │   │ mismatches   │   │ titles, disputes, │
│ key      │   │ and red      │   │ revocations,      │
│ fields   │   │ flags        │   │ acquisitions      │
└──────────┘   └──────────────┘   └───────────────────┘
    │                  │                   │
    └──────────────────┼───────────────────┘
                       ▼
          ┌────────────────────────┐
          │   RISK SCORING AGENT   │
          │                        │
          │  Assigns severity to   │
          │  each flag: Low /      │
          │  Medium / High /       │
          │  Critical              │
          └────────────┬───────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │   REPORT GENERATOR     │
          │                        │
          │  Produces downloadable │
          │  PDF / Markdown risk   │
          │  report with buyer     │
          │  checklist             │
          └────────────────────────┘
```

### Team Member and Their Roles

- **Antony Riziki** - Bulider/Engineer
- **Stephen Kibue** - Researcher
- **Pauline Kanyi** - Product Engineer
- **Eric Mbogo** -  UI/UX Designer
- **Evans Macharia** - Project Manager
- **Lucy Awino** - Product Designer

### Agents and Their Roles



| Agent | Tool(s) | Responsibility |
|---|---|---|
| **Orchestrator** | Google ADK | Manages session state, sequences agent calls, handles document flow |
| **Vision Agent** | Gemini Vision API | Extracts structured fields from document images (parcel no., seller name, acreage, dates, stamps, etc.) |
| **Consistency Agent** | Custom logic | Cross-checks extracted fields across all documents for mismatches |
| **Gazette Search Agent** | Google Search / web scraping | Queries Kenya Gazette for entries matching parcel numbers and seller names |
| **Risk Scoring Agent** | Rule engine + LLM | Assigns Low / Medium / High / Critical severity to each flag |
| **Report Generator** | Gemini (text) + PDF lib | Compiles all findings into a structured buyer-ready risk report |

### How Agents Communicate

- Each agent is a **Google ADK tool** registered with the Orchestrator.
- The Orchestrator passes the **transaction session object** (a structured JSON document containing all extracted fields and findings) between agents.
- Agents write back to the session object; downstream agents read from it.
- Firestore persists the session between steps so uploads and analysis can be asynchronous.

---

## What the Agent Extracts

From each uploaded document image, Gemini Vision pulls:

- Parcel number and title number
- Seller and buyer names
- National ID and KRA PIN numbers
- Registry location and land reference number
- Acreage / plot size
- Survey details and mutation numbers
- All dates (execution, registration, consent, transfer)
- Signature presence and stamp details
- Document type classification

---

## Risk Flags the Agent Detects

| Flag | Severity |
|---|---|
| Parcel number mismatch across documents | 🔴 High |
| Seller name differs between title deed and ID | 🔴 High |
| Acreage mismatch between survey map and title | 🔴 High |
| Parcel appears in Kenya Gazette lost title notice | 🔴 Critical |
| Parcel subject to compulsory acquisition notice | 🔴 Critical |
| Missing Land Control Board consent (agricultural land) | 🟡 Medium |
| Consent date appears after transfer date | 🟡 Medium |
| Suspicious document backdating indicators | 🟡 Medium |
| Conflicting KRA PIN across documents | 🟠 High |
| Duplicate or reused document serial numbers | 🟠 High |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Agent Orchestration | Google ADK |
| Document Vision | Gemini Vision (gemini-1.5-pro-vision) |
| Agent Workflows | Vertex AI Agent Builder |
| Document Storage | Google Cloud Storage |
| Session Persistence | Firestore |
| Backend API | FastAPI (Python) |
| Frontend | Next.js + React |
| Deployment | Cloud Run |
| Report Generation | ReportLab (PDF) |

---

## Running Locally

### Prerequisites

- Python 3.11+
- Node.js 18+
- Google Cloud project with Gemini API enabled
- A `.env` file (see `.env.example`)

### 1. Clone the repository

```bash
git clone https://github.com/your-org/mradi-wa-ardhi.git
cd mradi-wa-ardhi
```

### 2. Set up environment variables

```bash
cp .env.example .env
# Edit .env and add your keys:
# GOOGLE_API_KEY=...
# GOOGLE_CLOUD_PROJECT=...
# FIRESTORE_COLLECTION=transactions
```

### 3. Start the backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 4. Start the frontend

```bash
cd frontend
npm install
npm run dev
# Opens at http://localhost:3000
```

### 5. Test with sample documents

Sample land documents (anonymized) are in `/sample-docs/`. Upload them through the web UI to see a full risk report generated.

```bash
# Or test the API directly:
curl -X POST http://localhost:8000/api/transaction \
  -F "documents[]=@sample-docs/title_deed.jpg" \
  -F "documents[]=@sample-docs/sale_agreement.jpg"
```

---

## Interacting with the Deployed Version

**Live demo:** `https://mradi-wa-ardhi.run.app` *(link active during hackathon judging)*

### Workflow

1. **Create a transaction case** — enter a name or reference for the land deal
2. **Upload document photos** — take photos of any land documents you have (title deed, sale agreement, ID, survey map, etc.)
3. **Run analysis** — the agent extracts fields, checks consistency, and searches public records
4. **Review the risk report** — see each flag with its severity, explanation, and recommended action
5. **Download the report** — share with your lawyer or advocate

### API (for developers)

```
POST /api/transaction          # Create a new transaction case
POST /api/transaction/{id}/documents  # Upload documents
GET  /api/transaction/{id}/report     # Get risk report (JSON)
GET  /api/transaction/{id}/report/pdf # Download PDF report
```

---

## 📸 Screenshots & Demo

> 📹 **Demo Video:** [Watch on YouTube →](https://youtube.com/your-demo-link)

| Step | Screenshot |
|---|---|
| Document upload interface | *(coming soon)* |
| Extracted fields view | *(coming soon)* |
| Risk flags dashboard | *(coming soon)* |
| Final PDF report | *(coming soon)* |

*Screenshots will be added before final submission.*


---

## 📋 Project Status (MVP)

- [x] Document upload and session management
- [x] Gemini Vision field extraction
- [x] Cross-document consistency checks
- [x] Kenya Gazette search integration
- [x] Risk scoring (Low / Medium / High / Critical)
- [x] PDF risk report generation
- [x] Buyer checklist
- [ ] County rates and land rent verification *(roadmap)*
- [ ] Official land registry API integration *(roadmap, pending availability)*
- [ ] Map-based parcel visualization *(roadmap)*
- [ ] WhatsApp report delivery *(roadmap)*

---

## Disclaimer

Mradi wa Ardhi is a risk-screening assistant. It does **not** replace a licensed advocate, registered surveyor, land registrar, or official government search. Always have land transactions reviewed by a qualified professional before signing or making payments.

---

## 📄 License

MIT License — see [LICENSE](./LICENSE)
