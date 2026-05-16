# Mradi wa Ardhi — Land Transaction Risk Agent

## Overview

**Mradi wa Ardhi** is an AI-powered land transaction stress-testing agent for Kenya. It helps buyers, lawyers, agents, and families detect potential land fraud before signing a land purchase agreement.

Land fraud is one of Kenya’s most expensive crimes. A single land transaction can involve title deeds, parcel searches, sale agreements, ID documents, PIN certificates, land control board approvals, mutation forms, maps, rates clearance certificates, and Kenya Gazette notices. Many of these documents can be forged, altered, backdated, or mismatched.

This agent reviews uploaded document photos, extracts key details using Gemini Vision, cross-checks inconsistencies, searches public records such as the Kenya Gazette, and generates a transaction risk report.

---

## Suggested Local Solution Names

### Top Picks

1. **HakiArdhi** — land justice
2. **Mlinzi wa Ardhi** — land guardian
3. **ArdhiSalama** — safe land
4. **Macho ya Ardhi** — eyes of the land
5. **ChekiTitle** — casual Kenyan-style title verification

### Other Name Ideas

- **Thibitisha Ardhi** — verify land
- **KaguaPlot** — inspect the plot
- **LindaPlot** — protect the plot
- **Ukweli wa Ardhi** — truth of land
- **JiraniCheck** — community-style verification
- **BomaVerify** — home/land verification
- **RamaniTrust** — map plus trust
- **PlotSafi** — clean plot
- **ArdhiRadar** — detects hidden risk
- **TitleMlinzi** — title deed guardian
- **MziziArdhi** — land roots
- **KipimoArdhi** — land test or measure
- **UsalamaPlot** — plot safety

Recommended brand name: **HakiArdhi**  
Recommended product tagline: **Verify before you buy.**

---

## Problem Statement

Buying land in Kenya is risky because buyers often rely on documents that may be incomplete, forged, inconsistent, or outdated. Fraudsters may exploit gaps between paper records, registry records, Gazette notices, land maps, and seller identity documents.

The goal of this project is to build an AI agent that helps detect red flags before money changes hands.

---

## Core Features

### 1. Document Upload and Vision Extraction

Users upload photos or scans of land transaction documents. Gemini Vision extracts:

- Parcel number
- Title number
- Land reference number
- Seller name
- Buyer name
- ID number
- KRA PIN
- Registry location
- Acreage or plot size
- Survey details
- Dates and signatures
- Stamp details
- Document type

### 2. Cross-Document Consistency Checks

The agent compares extracted information across all uploaded documents and flags issues such as:

- Parcel number mismatch
- Seller name mismatch
- Different acreage across documents
- Suspicious date sequence
- Missing consent documents
- Conflicting registry locations
- Backdated or altered-looking documents
- Different ID or KRA PIN values
- Duplicate or reused document numbers

### 3. Kenya Gazette Search

The agent searches the Kenya Gazette for relevant entries such as:

- Lost title notices
- Revocation notices
- Court disputes
- Succession matters
- Compulsory acquisition notices
- Land adjudication notices
- Boundary or survey disputes

### 4. Risk Scoring

Each transaction receives a structured risk score:

- **Low Risk** — no major inconsistencies found
- **Medium Risk** — some missing or inconsistent information
- **High Risk** — serious red flags detected
- **Critical Risk** — likely fraud indicators or major unresolved conflicts

### 5. Risk Report Generation

The final report includes:

- Transaction summary
- Extracted document data
- Inconsistency table
- Gazette findings
- Missing documents
- Fraud red flags
- Recommended next steps
- Buyer checklist
- Lawyer/advocate review notes

---

## Suggested Tech Stack

- **Google ADK** — agent orchestration
- **Gemini Vision** — document image reading and extraction
- **Vertex AI Agent Builder** — multi-step agent workflows
- **Google Cloud Storage** — document upload storage
- **Firestore** — transaction session storage
- **Cloud Run** — backend deployment
- **Antigravity** — rapid app prototyping
- **Next.js or React** — frontend interface
- **FastAPI or Node.js** — backend API

---

## Agent Workflow

1. User creates a transaction case.
2. User uploads land-related documents.
3. Gemini Vision extracts key fields from each image.
4. Agent normalizes extracted values.
5. Agent compares all documents for inconsistencies.
6. Agent searches public references such as the Kenya Gazette.
7. Agent assigns risk categories to each issue.
8. Agent generates a final buyer-ready risk report.

---

## Example Risk Flags

| Risk Flag | Severity | Example |
|---|---:|---|
| Parcel number mismatch | High | Title deed shows one parcel number, sale agreement shows another |
| Seller identity mismatch | High | Seller name differs between title and ID |
| Gazette lost-title notice | Critical | Parcel appears in a lost title notice |
| Missing Land Control Board consent | Medium | Agricultural land transaction lacks consent evidence |
| Suspicious document dates | Medium | Consent date appears after transfer date |
| Acreage mismatch | High | Survey map and title show different land sizes |

---

## MVP Scope

The minimum viable product should support:

- Uploading document photos
- Extracting key land transaction fields
- Detecting document inconsistencies
- Searching Gazette references manually or automatically
- Generating a downloadable PDF or Markdown risk report
- Providing a buyer checklist

---

## Future Improvements

- Integration with official land registry APIs if available
- County rates and land rent verification
- Advocate dashboard
- Seller risk history
- Map-based parcel visualization
- Blockchain-backed audit trail
- SMS/WhatsApp report delivery
- Community dispute reporting layer

---

## Disclaimer

This tool does not replace a licensed advocate, surveyor, land registrar, or official government search. It is a risk-screening assistant designed to help buyers identify issues that require professional verification before signing or paying.

---

## License

MIT License

