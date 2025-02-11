from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, este es el backend del chatbot!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    # Lógica básica de respuestas
    responses = {
        "hola": "Hola! Como puedo ayudarte?",
        "como estas": "Estoy bien, gracias por preguntar.",
        "adios": "Hasta luego!"
    }

    # Buscar una respuesta basada en el mensaje del usuario
    bot_response = responses.get(user_message, "Lo siento, no entiendo la pregunta.")

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)