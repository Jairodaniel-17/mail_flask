# Documentación del Proyecto Flask-Mail
## Descripción
El proyecto es un servicio porque proporciona funcionalidades específicas de envío de correos electrónicos a través de una API definida y fácil de usar, operando sobre la infraestructura web de Flask. Es especialmente útil en aplicaciones donde se requieren notificaciones automáticas, como sistemas de registro de usuarios, confirmaciones de pedidos en comercios electrónicos, o alertas automáticas en sistemas de monitoreo. Gracias a su configurabilidad y la integración con Flask-Mail, se adapta eficientemente a diferentes entornos y necesidades de negocio.

# Requerimientos del Sistema y Dependencias del Proyecto
A continuación, se detalla la estructura y funcionalidad de cada uno de los archivos que componen el proyecto:

## app.py
Este es el archivo principal de la aplicación. Aquí se define la instancia de la aplicación Flask y se configura el servicio de correo utilizando Flask-Mail. Este archivo contiene:

- Configuración inicial de Flask.
- Configuración de Flask-Mail con variables de entorno.
- Definición de la ruta `/send_mail` que acepta solicitudes POST para enviar correos electrónicos, utilizando los datos proporcionados en el formato especificado por `EmailSchema`.

## estructura_correo.py
Este archivo utiliza Pydantic para definir la estructura de datos de los correos electrónicos a través de la clase `EmailSchema`, que incluye:

- `subject`: Asunto del correo electrónico.
- `sender`: Correo electrónico del remitente (se define en las variables de entorno, no se requiere declarar( ***opcional***)).
- `recipients`: Lista de correos electrónicos de los destinatarios.
- `cc`: Lista de correos electrónicos de los destinatarios en copia (opcional).
- `body`: Cuerpo del correo electrónico.

## .env
Archivo que almacena las variables de entorno necesarias para la configuración del servidor de correo, incluyendo:

- `MAIL_SERVER`: Servidor de correo electrónico.
- `MAIL_PORT`: Puerto utilizado por el servidor de correo.
- `MAIL_USE_TLS`: Indica si se utiliza TLS.
- `MAIL_USERNAME`: Nombre de usuario para la autenticación en el servidor de correo.
- `MAIL_PASSWORD`: Contraseña para la autenticación en el servidor de correo.

## .gitignore
Archivo utilizado por Git para ignorar archivos y directorios que no deben ser incluidos en el control de versiones, tales como:

- Archivos de entorno virtual (`.venv/`).
- Archivos de configuración local (`.env`).
- Archivos temporales o de log (`__pycache__`).

## requirements.txt
Lista de todas las dependencias necesarias para ejecutar el proyecto, las cuales pueden instalarse utilizando el comando `pip install -r requirements.txt`. Incluye:

- Flask
- Flask-Mail
- Pydantic
- Otros paquetes necesarios
