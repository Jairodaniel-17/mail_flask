# esta es la estructura del json que se espera recibir en el endpoint /send_mail
from model.estructura_correo import EmailSchema


obj = EmailSchema(
    subject="Asunto del Correo, ejemplo",
    recipients=["ejemplo@untels.edu.pe", "ejemplo@gmail.com"],
    cc=["ejemplo@hotmail.com", "ejemplo@outlook.com"],
    body="ejemplo, Este es el cuerpo del correo. Puedes incluir el texto que desees aqui.",
)
print(obj.model_dump_json())
# guardar el json en un archivo para poder usarlo en el test de la API
with open("test.json", "w") as f:
    f.write(obj.model_dump_json())
