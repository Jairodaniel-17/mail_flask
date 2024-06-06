from datetime import datetime
from pydantic import ValidationError
from werkzeug.utils import secure_filename
from model.estructura_correo import EmailSchema
from flask import Flask, request, jsonify, render_template_string
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import logging


logging.basicConfig(level=logging.INFO)

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


def render_email(template_name, **context):
    """Renderiza una plantilla HTML para el correo electrónico"""
    return render_template_string(template_name, **context)


@app.route("/")
def index():
    return "API para gestionar correos"


@app.route("/send_mail", methods=["POST"])
def send_mail():
    try:
        data = EmailSchema(**request.get_json())
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

    try:
        html_body = render_email(
            "<h2>Mensaje automatico,</h2><p>{{ body }}</p>", body=data.body
        )
        msg = Message(
            subject=f"{data.subject} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            sender=data.sender or app.config["MAIL_DEFAULT_SENDER"],
            recipients=data.recipients,
            cc=data.cc,
            bcc=data.cco,
            body=data.body,
            html=html_body,
        )
        mail.send(msg)
    except Exception as e:
        app.logger.error(f"Failed to send email: {str(e)}")
        return jsonify({"error": "Failed to send email due to an internal error."}), 500

    return jsonify({"message": "Correo enviado exitosamente"}), 200


@app.route("/send_mail_with_attachments", methods=["POST"])
def send_mail_with_attachments():
    try:
        data = EmailSchema(**request.get_json())
        files = request.files.getlist("attachments")
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

    try:
        html_body = render_email(
            "<h2>Mensaje automatico,</h2><p>{{ body }}</p>", body=data.body
        )
        msg = Message(
            subject=data.subject,
            sender=data.sender,
            recipients=data.recipients,
            cc=data.cc,
            bcc=data.cco,
            body=data.body,
            html=html_body,
        )

        for file in files:
            filename = secure_filename(file.filename)
            mimetype = file.content_type
            with file.stream as fp:
                msg.attach(filename, mimetype, fp.read())

        mail.send(msg)
    except Exception as e:
        app.logger.error(f"Failed to send email with attachments: {str(e)}")
        return jsonify({"error": "Failed to send email due to an internal error."}), 500

    return jsonify({"message": "Correo enviado exitosamente con adjuntos"}), 200


if __name__ == "__main__":
    app.run(port=10001)
