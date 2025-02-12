import React from "react";
import Chatbot from "./components/Chatbot"; // 👈 Asegúrate de importar bien Chatbot.js

function App() {
    return (
        <div>
            <h1 style={{ textAlign: "center" }}>Chatbot IA</h1>
            <Chatbot />
        </div>
    );
}

export default App;