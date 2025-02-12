import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    const sendMessage = async () => {
        if (!input.trim()) return;

        const userMessage = { text: input, sender: "user" };
        setMessages([...messages, userMessage]);

        try {
            const response = await axios.post("http://127.0.0.1:5000/chat", {
                message: input,
            });

            const botMessage = { text: response.data.response, sender: "bot" };
            setMessages([...messages, userMessage, botMessage]);
        } catch (error) {
            console.error("Error:", error);
        }

        setInput("");
    };

    return (
        <div style={styles.container}>
            <div style={styles.chatbox}>
                {messages.map((msg, index) => (
                    <div
                        key={index}
                        style={{
                            ...styles.message,
                            backgroundColor: msg.sender === "user" ? "#007bff" : "#28a745",
                            alignSelf: msg.sender === "user" ? "flex-end" : "flex-start",
                        }}
                    >
                        {msg.text}
                    </div>
                ))}
            </div>
            <div style={styles.inputContainer}>
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    style={styles.input}
                    placeholder="Escribe un mensaje..."
                />
                <button onClick={sendMessage} style={styles.button}>Enviar</button>
            </div>
        </div>
    );
};

const styles = {
    container: { display: "flex", flexDirection: "column", width: "300px", margin: "auto", marginTop: "50px" },
    chatbox: { display: "flex", flexDirection: "column", height: "400px", border: "1px solid #ccc", padding: "10px", overflowY: "auto" },
    message: { padding: "10px", borderRadius: "10px", color: "white", margin: "5px", maxWidth: "80%" },
    inputContainer: { display: "flex", marginTop: "10px" },
    input: { flex: 1, padding: "10px", border: "1px solid #ccc", borderRadius: "5px" },
    button: { padding: "10px", marginLeft: "5px", border: "none", backgroundColor: "#007bff", color: "white", borderRadius: "5px", cursor: "pointer" }
};

export default Chatbot;