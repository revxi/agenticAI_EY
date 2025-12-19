# 🛸 FinAI: Agentic Loanflow Prototype

**FinAI** is a high-fidelity, multi-agent conversational AI system designed to automate the end-to-end loan application lifecycle. It features a specialized **Master Orchestrator** that manages state transitions across four distinct AI agents, wrapped in a "Classy Sci-Fi" terminal interface.



---

## 🌟 Key Features

* **Multi-Agent Orchestration:** Linear state-machine handoffs between Sales, KYC, Underwriting, and Document agents.
* **Sci-Fi UI/UX:** A React-based terminal featuring a Matrix-style binary background (Canvas API) and neon-green glow effects.
* **Mock Verification Services:** Simulated API integrations for PAN/Aadhaar identity checks and credit scoring.
* **Dynamic Document Generation:** Automated production of a digital Sanction Letter (Mock PDF) upon approval.

---
finai/
├── .gitignore               # Prevents node_modules, venv, and .env from being uploaded
├── README.md                # The visual guide and documentation we just wrote
├── LICENSE                  # MIT License
├── CONTRIBUTORS.md          # Credits for you and your AI partner
├── Makefile                 # Shortcuts for running backend and frontend simultaneously
│
├── backend/                 # FastAPI Logic
│   ├── main.py              # API Routes and Session handling
│   ├── requirements.txt     # Python dependencies
│   ├── .env                 # API Keys (Local only, not on GitHub)
│   ├── agents/              # The "Brain" (Multi-Agent logic)
│   │   ├── master.py        # The Orchestrator / State Machine
│   │   ├── sales.py         # Humanizer Agent
│   │   ├── verification.py  # KYC Agent
│   │   ├── underwriting.py  # Risk Agent
│   │   └── sanction.py      # Document Agent
│   ├── services/            # Mock external integrations
│   │   ├── credit_api.py    # Mock KYC/Credit Score fetching
│   │   └── pdf_generator.py # Mock PDF Sanction Letter creation
│   └── models/
│       └── loan_schema.py   # Shared Pydantic data structures
│
└── frontend/                # React.js UI
    ├── package.json         # Node dependencies and scripts
    ├── public/
    │   └── index.html       # Entry HTML (Head/Meta tags)
    └── src/
        ├── App.js           # Core state management & API calls
        ├── App.css          # Sci-Fi styling (Glows, Neon Green, Dark mode)
        ├── index.js         # React DOM renderer
        └── components/      # UI Modular pieces
            ├── BinaryBackground.js  # Canvas Matrix-style animation
            ├── ChatBox.js           # Message display logic
            └── MessageInput.js      # Sci-fi styled terminal input

## 🏗️ System Architecture

The core of FinAI is a **Linear Workflow Agentic Design**. Each agent is responsible for a specific state in the lifecycle:

| Agent | State | Responsibility |
| :--- | :--- | :--- |
| **Sales (Humanizer)** | `SALES` | Rapport building and initial requirement gathering. |
| **Verification (KYC)** | `KYC_REQUIRED` | Identity validation using mock PAN/Aadhaar data. |
| **Underwriting** | `UNDERWRITING` | Risk assessment via mock credit score and income-to-debt rules. |
| **Document Agent** | `DECISION_READY` | Final letter generation and storage handling. |



---

## 📊 Underwriting Logic (The "Brain")

The system calculates loan eligibility using specific financial guardrails:

### Approval Conditions
* $\text{Credit Score} \ge 650$
* $\text{Annual Income} \ge 40,000$

### Sanction Calculation
$$\text{Max Approved} = \min(\text{Requested Amount}, \text{Annual Income} \times 4.5)$$

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python), Pydantic (Schema Validation), Uvicorn.
* **Frontend:** React.js, HTML5 Canvas (Binary Animation), CSS Modules (Sci-Fi Theme).
* **Agents:** Custom state-machine logic with LLM-ready prompts.
* **Services:** Mock API simulation for Credit and PDF generation.

---

## 🚀 Installation & Setup

### 1. Prerequisites
* Python 3.9+
* Node.js & npm

### 2. Backend Installation
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
3. Frontend Installation
Bash

cd frontend
npm install
npm start
```
🎨 Visual Identity
Font: 'Share Tech Mono' (Retro-Terminal)

Theme: Matrix Green (#00ff00) on Deep Space Gray (#1a1a1a).

Background: Real-time animated binary digit stream.

👥 Contributors
reverie - Lead Architect & Full-Stack Developer

Gemini - AI Thought Partner & Logic Implementation

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer: This is a technical prototype. All financial data and documents are mock-ups for demonstration purposes only. Do not enter real PII.


---

