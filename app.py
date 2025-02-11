from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, este es el backend del chatbot!"

if __name__ == "__main__":
    app.run(debug=True)