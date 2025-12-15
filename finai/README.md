<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agentic LoanFlow Demo</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            background-color: #f4f7f6;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .chat-container {
            width: 100%;
            max-width: 600px;
            background: #fff;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            border-radius: 12px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            max-height: 90vh;
        }
        .chat-header {
            background-color: #007bff;
            color: white;
            padding: 15px;
            font-size: 1.2em;
            text-align: center;
            font-weight: 600;
        }
        .chat-box {
            flex-grow: 1;
            padding: 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        .message {
            max-width: 80%;
            padding: 10px 15px;
            border-radius: 18px;
            line-height: 1.4;
        }
        .user-message {
            align-self: flex-end;
            background-color: #007bff;
            color: white;
            border-bottom-right-radius: 2px;
        }
        .agent-message {
            align-self: flex-start;
            background-color: #e0e0e0;
            color: #333;
            border-bottom-left-radius: 2px;
        }
        .input-area {
            display: flex;
            padding: 15px;
            border-top: 1px solid #eee;
        }
        .input-area input {
            flex-grow: 1;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 20px;
            margin-right: 10px;
            font-size: 1em;
        }
        .input-area button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 20px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .input-area button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

<div class="chat-container">
    <div class="chat-header">
        Agentic LoanFlow Prototype
    </div>
    <div class="chat-box" id="chat-box">
        </div>
    <div class="input-area">
        <input type="text" id="user-input" placeholder="Type your message...">
        <button onclick="sendMessage()">Send</button>
    </div>
</div>

<script>
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const API_URL = 'http://127.0.0.1:8000'; // Match your FastAPI server location
    let conversation_id = null; // To track the session

    // --- Utility Functions ---

    function displayMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(sender === 'user' ? 'user-message' : 'agent-message');
        
        // Basic Markdown-to-HTML conversion for links/bold
        let formattedText = text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\[Link to PDF\]\((.*?)\)/g, '<a href="$1" target="_blank">Download Sanction Letter (Mock PDF)</a>');

        messageDiv.innerHTML = formattedText;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
    }

    function startChat() {
        // Send an empty message to the /start endpoint to initialize the Orchestrator
        fetch(`${API_URL}/start`, { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                conversation_id = data.conversation_id;
                displayMessage(data.response, 'agent');
            })
            .catch(error => {
                displayMessage('Error connecting to the backend. Is the FastAPI server running?', 'agent');
                console.error('Error starting chat:', error);
            });
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        displayMessage(message, 'user');
        userInput.value = ''; // Clear input

        if (!conversation_id) {
            displayMessage('Please start the chat session first.', 'agent');
            return;
        }

        // Send the user message to the /chat endpoint
        fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                conversation_id: conversation_id,
                message: message
            })
        })
        .then(response => response.json())
        .then(data => {
            displayMessage(data.response, 'agent');
        })
        .catch(error => {
            displayMessage('An error occurred during processing. Please try again.', 'agent');
            console.error('Error processing message:', error);
        });
    }

    // Allow sending message by pressing Enter
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Start the chat automatically when the page loads
    window.onload = startChat;
</script>

</body>
</html>