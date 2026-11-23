# API de Gestión de Usuarios (User Management API)

API REST desarrollada con Python y FastAPI para administrar usuarios, almacenar información en MongoDB Atlas e integrar inteligencia artificial mediante Google Gemini.

## Características principales

- Crear usuarios.
- Consultar todos los usuarios registrados.
- Consultar usuarios por su identificador.
- Actualizar información de usuarios.
- Eliminar usuarios.
- Almacenamiento persistente mediante MongoDB Atlas.
- Validación de datos utilizando Pydantic.
- Autenticación mediante API Key para proteger los endpoints.
- Integración con Google Gemini AI para responder preguntas relacionadas con los usuarios registrados.
- Documentación interactiva mediante Swagger UI.

## Tecnologías utilizadas

- **Python:** lenguaje principal de programación.
- **FastAPI:** framework para desarrollar la API REST.
- **MongoDB Atlas:** base de datos NoSQL en la nube.
- **PyMongo:** conexión y comunicación con MongoDB.
- **Pydantic:** validación y estructuración de datos.
- **Google Gemini AI:** integración de inteligencia artificial.
- **Python-dotenv:** gestión de variables de entorno.
- **Git y GitHub:** control de versiones y alojamiento del código.

## Estructura del proyecto

```text
user-management-api/
│
├── main.py
├── database.py
├── ia_service.py
├── gemini_test.py
├── .git
