import os
from flask import Flask, request, jsonify
from gpt4all import GPT4All
from flask_cors import CORS  # Permitir conexiones desde el frontend

app = Flask(__name__)
CORS(app)  # Habilitar CORS para evitar problemas con React

# Ruta del modelo (AJUSTA SI ES NECESARIO)
MODEL_PATH = "/Users/alesia565/Library/Application Support/nomic.ai/GPT4All/Meta-Llama-3-8B-Instruct.Q4_0.gguf"

# Verificar si el modelo existe antes de cargarlo
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ El modelo no se encuentra en {MODEL_PATH}. Verifica su ubicación.")

# Cargar el modelo GPT4All
model = GPT4All(MODEL_PATH)

@app.route('/chat', methods=['POST'])
def chat():
    """Recibe un mensaje JSON con 'message' y devuelve la respuesta generada."""
    data = request.json
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "⚠️ Mensaje vacío"}), 400

    try:
        # Prompt optimizado para respuestas cortas y sin etiquetas "Usuario / Asistente"
        system_prompt = "Responde en español, de forma breve y clara, sin agregar etiquetas como 'Usuario' o 'Asistente'. Solo responde con la información relevante en menos de 30 palabras."

        # Generar respuesta optimizada
        response = model.generate(f"{system_prompt}\nPregunta: {user_input}\nRespuesta:", 
                                  max_tokens=50, temp=0.5)

        # Filtrar posibles respuestas incorrectas
        clean_response = response.replace("Pregunta:", "").replace("Respuesta:", "").strip()

        return jsonify({"response": clean_response})

    except Exception as e:
        return jsonify({"error": f"⚠️ Error en el modelo: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)  # Flask corre en el puerto 5001