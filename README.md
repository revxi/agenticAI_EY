
🛸 FinAI: Agentic Loan Origination System
FinAI is a high-fidelity, multi-agent AI prototype designed to automate the end-to-end loan application lifecycle. It features a specialized Master Orchestrator that manages state transitions across four distinct AI agents, providing a seamless "classy sci-fi" terminal experience for the user.
🌟 Key Features
 * Multi-Agent Orchestration: A centralized state machine that hands off the conversation between specialized agents.
 * Sci-Fi UI: A React-based frontend featuring a Matrix-style binary digit background animation (Canvas API).
 * Automated KYC: Mock integration for PAN and Aadhaar verification.
 * Rule-Based Underwriting: Real-time risk assessment and decision-making logic.
 * Document Generation: Automated production of a digital Sanction Letter (Mock PDF).
🏗️ Architecture & Agent Roles
The system is built on a linear workflow where each agent is responsible for a specific stage of the loan lifecycle:
| Agent | Stage | Responsibility |
|---|---|---|
| Humanizer (Sales) | SALES | Rapport building and capturing loan requirements (amount, purpose). |
| Verification (KYC) | KYC_REQUIRED | Collecting and validating identification documents (PAN/Aadhaar). |
| Underwriting | UNDERWRITING | Analyzing credit scores and income to approve or reject the loan. |
| Document Agent | DECISION_READY | Generating the final legal mock-up and download link. |
🛠️ Tech Stack
 * Backend: FastAPI (Python 3.9+), Pydantic, Uvicorn
 * Frontend: React.js, HTML5 Canvas, CSS3 (Glow & Terminal effects)
 * Data Models: State-persistent Pydantic schemas
 * Services: Mock Credit API & Mock PDF Generator
🚀 Installation & Setup
1. Backend Setup
Navigate to the backend directory and set up your environment:
cd backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

2. Frontend Setup
In a new terminal, set up the React application:
cd frontend
npm install
npm start

3. Environment Variables
Create a .env file in the root directory to store your LLM configuration:
OPENAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here

📊 Underwriting Logic
The Underwriting Agent evaluates the application based on the following mock financial logic:
Approval Conditions
A loan is approved only if:
 *  * Sanction Calculation
The approved amount is calculated as:

Interest Rate Tiers
 * Tier 1 (Score \ge 750): 7.5\%
 * Tier 2 (650 \le Score < 750): 9.5\%
🖥️ UI Preview
 * Background: Dynamic binary stream rendered via HTML5 Canvas.
 * Typography: 'Share Tech Mono' for that retro-future terminal feel.
 * Colors: #00ff00 (Matrix Green) on #1a1a1a (Deep Space Gray).
⚠️ Disclaimer
This project is a technical prototype. * It does not connect to real credit bureaus or banking backends.
 * All PDF documents generated are mock-ups and have no legal standing.
 * Do not enter real PII (Personally Identifiable Information) in this demo.
Would you like me to create a LICENSE file or a CONTRIBUTING.md file to make the repo even more official?
