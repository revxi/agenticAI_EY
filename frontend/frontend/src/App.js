import React, { useEffect, useState } from 'react';
import './App.css';
import BinaryBackground from './components/BinaryBackground';
import ChatBox from './components/ChatBox';
import MessageInput from './components/MessageInput';

function App() {
  const [messages, setMessages] = useState([]);
  const [sessionId, setSessionId] = useState(null);

  const API_BASE = process.env.REACT_APP_API_URL || '';

  useEffect(() => {
    async function start() {
      try {
        const res = await fetch(`${API_BASE || ''}/start`, { method: 'POST' });
        const data = await res.json();
        setSessionId(data.conversation_id);
        setMessages([{ from: 'bot', text: data.response }]);
      } catch (e) {
        setMessages([{ from: 'bot', text: 'Backend unreachable' }]);
      }
    }
    start();
  }, [API_BASE]);

  async function sendMessage(text) {
    setMessages((m) => [...m, { from: 'user', text }]);

    try {
      const res = await fetch(`${API_BASE || ''}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ conversation_id: sessionId, message: text }),
      });
      const data = await res.json();
      setMessages((m) => [...m, { from: 'bot', text: data.response }]);
    } catch (e) {
      setMessages((m) => [...m, { from: 'bot', text: 'Error contacting backend' }]);
    }
  }

  return (
    <div className="app-container">
      <BinaryBackground />

      <div className="glass-card">
        <h1 className="title">Agentic LoanFlow Prototype (React)</h1>

        <div className="status-indicator">
          <span>Current Stage:</span>
          <span className="status-text">Sales Agent Active</span>
        </div>

        <ChatBox messages={messages} />

        <MessageInput onSend={sendMessage} />
      </div>
    </div>
  );
}

export default App;
