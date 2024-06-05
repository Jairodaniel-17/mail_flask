from datetime import datetime
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
from pydantic import ValidationError
from model.estructura_correo import EmailSchema

load_dotenv()

app = Flask(__name__)
app.config.update(
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_USE_TLS=os.getenv("MAIL_USE_TLS") == "True",
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
)

mail = Mail(app)


@app.route("/")
def index():
    return "API para gestionar correos"


@app.route("/send_mail", methods=["POST"])
def send_mail():
    try:
        data = EmailSchema(**request.get_json())
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

    msg = Message(
        data.subject,
        sender=data.sender,
        recipients=data.recipients,
        bcc=data.cco,
        cc=data.cc,
        body=data.body,
        date=datetime.now(),
    )
    mail.send(msg)
    return jsonify({"message": "Correo enviado exitosamente"}), 200


@app.route("/send_mail", methods=["GET"])
def bienvenida_mail():
    return jsonify({"message": "Bienvenido a la API para enviar correos"}), 200


if __name__ == "__main__":
    app.run(port=10000)
