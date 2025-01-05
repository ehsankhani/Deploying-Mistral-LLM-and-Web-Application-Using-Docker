import React, { useState } from "react";
import axios from "axios";

const Chat = () => {
    const [history, setHistory] = useState("");
    const [question, setQuestion] = useState("");
    const [response, setResponse] = useState("");

    const sendMessage = async () => {
        try {
            const res = await axios.post("http://localhost:5000/api/chat", {
                history,
                question,
            });
            setResponse(res.data.response);
            setHistory((prev) => `${prev}User: ${question}\nAI: ${res.data.response}\n`);
            setQuestion("");
        } catch (error) {
            setResponse("Error: " + error.message);
        }
    };

    return (
        <div>
            <h1>Chat with AI</h1>
            <div>
                <textarea value={history} readOnly rows="10" cols="50" />
            </div>
            <div>
                <input
                    type="text"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    placeholder="Type your question..."
                />
                <button onClick={sendMessage}>Send</button>
            </div>
            <div>
                <h3>AI Response:</h3>
                <p>{response}</p>
            </div>
        </div>
    );
};

export default Chat;
