 💡 Agentic LoanFlow Prototype
 A Multi-Agent AI System for Automated Loan Origination

| Status | Prototype/Demo |
| :--- | :--- |
| **Architecture** | Multi-Agent System (MAS) |
| **Core Function** | Automated Sales, KYC, Underwriting, & Sanction Letter Generation |
| **Technology Focus** | Agent Coordination, State Management, and Conversational AI |

This repository hosts Agentic LoanFlow, a working prototype that demonstrates a fully automated, conversational workflow for processing a personal loan application. It models a complex business process (loan origination) using a sophisticated **multi-agent architecture** coordinated by a central orchestrator.

The system guides a user through the entire process—from initial sales inquiry to the final decision and production of a mock PDF sanction letter—all within a single, continuous chat interface.
 🏗️ System Architecture

The project is built on **five specialized, coordinated AI Agents** managed by a central **Master Orchestrator**. This modular design ensures that each complex stage of the loan process is handled by an expert component.

| Agent Role | Workflow Stage | Key Responsibility |
| :--- | :--- | :--- |
| **Loan Orchestrator (Master)** | Control & Coordination | Manages state, routes the conversation, and aggregates the final outcome. |
| **Humanizer Agent** | Sales & Inquiry | Chats like a human, assesses needs (amount, purpose), and builds rapport. |
| **KYC Agent** | Identity Verification | Simulates collection and validation of required mock ID/KYC data via a Mock API. |
| **Underwriting Agent** | Risk Assessment | Applies mock rules based on income/credit score to approve or reject the loan and determine terms. |
| **Document Agent** | Output Generation | Formats the final approved terms into a downloadable **Mock PDF Sanction Letter**. |

 🔄 Agentic Workflow Flowchart

1.  **User Interaction** $\to$ **Humanizer Agent** (Gathers requirements)
2.  **Humanizer $\to$ Loan Orchestrator** (Data Handoff)
3.  **Orchestrator $\to$ KYC Agent** (Requests mock ID details)
4.  **KYC Agent $\to$ Orchestrator** (Mock verification complete)
5.  **Orchestrator $\to$ Underwriting Agent** (Requests mock financial data, applies rules)
6.  **Underwriting Agent $\to$ Orchestrator** (Delivers final decision and terms)
7.  **Orchestrator $\to$ Document Agent** (Triggers PDF generation)
8.  **Document Agent $\to$ Orchestrator** (Returns PDF link)
9.  **Orchestrator $\to$ User** (Presents final, humanized result and PDF link)

🚀 Getting Started

Follow these steps to get the Agentic LoanFlow prototype running locally.

 Prerequisites

  * Python (3.9+)
  * `pip` package manager
  * An API Key for your preferred LLM provider (e.g., OpenAI, Google Gemini, Anthropic).

 Installation

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/YourUsername/agentic-loanflow-prototype.git
    cd agentic-loanflow-prototype
    ```

2.  **Set up Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Key:**
    Create a file named `.env` in the root directory and add your API key.

    ***.env***

    ```
    # Replace with your actual key
    OPENAI_API_KEY="sk-..." 
    # OR 
    GEMINI_API_KEY="AIza..."
    ```

### Running the Demo

1.  **Start the Master Agent:**
    The core demo can be started via the main script.

    ```bash
    python run_orchestrator.py
    ```

2.  **Start Chatting:**
    The console will prompt you to begin the application.

    > **Example Interaction:**
    > **User:** "I need a loan to buy a new computer."
    > **Humanizer:** "That sounds exciting\! How much financing do you need, and can you briefly tell me about your employment status?"
## 🛠️ Mock APIs and Logic

To function as a safe and isolated prototype, this system uses simulated logic:

### 1\. Mock KYC Validation

The KYC Agent uses a dummy function that always returns `VALID` if the input format matches a standard ID number pattern (e.g., 10 alphanumeric characters for PAN).

### 2\. Mock Underwriting Rules

The Underwriting Agent follows a simple mock decision matrix:

  * **Approval Condition:** `(Mock Credit Score >= 700)` AND `(Annual Income >= $50,000)`
  * **Sanctioned Amount:** Calculated as `8x` the Annual Income, capped at $100,000.
  * **Interest Rate:** Fixed at a prototype rate of **$9.5\%$**.

### 3\. Mock PDF Generation

The Document Agent uses a basic library to generate a simple, static PDF structure. The link provided to the user will point to a locally generated file (e.g., `sanction_letter_[timestamp].pdf`).

-----

## ⚠️ Important Disclaimer

**This is a research and demo prototype only.** It uses simulated data, mock API calls, and dummy financial criteria. It is **not** a real banking application, nor is it connected to any real-world financial, identity verification, or credit reporting systems. **DO NOT** enter any real personal or financial information.
