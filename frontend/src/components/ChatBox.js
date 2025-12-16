import React from "react";
import "./ChatBox.css";

const ChatBox = ({ messages = [] }) => {
  return (
    <div className="chat-box">
      {messages.map((m, i) => (
        <div key={i} className={`message ${m.from}`}>
          {m.text}
        </div>
      ))}
    </div>
  );
};

export default ChatBox;
