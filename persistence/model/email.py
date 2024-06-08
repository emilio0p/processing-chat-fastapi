from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List
from dotenv import load_dotenv
import os

# Cargamos el .env
load_dotenv()

# String de conexión
EMAIL = os.getenv("EMAIL")
EMAIL_PASS = os.getenv("EMAIL_PASS")

class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME = EMAIL,  # Your Hotmail email address
    MAIL_PASSWORD = EMAIL_PASS,  # Replace with your Hotmail App Password
    MAIL_FROM = EMAIL,
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.office365.com",  # Correct SMTP server for Hotmail
    MAIL_FROM_NAME="",  # Your desired sender name
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)