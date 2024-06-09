# Importaciones
# Importaciones
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel

from connection.connect import get_db
from persistence.model.user_dto import UserDTO, UserAddDTO
from persistence.model.json_dto import JSONResp
from service.auth_service import register_user, check_login, current_user
from persistence.model.email import conf
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from jinja2 import Environment, PackageLoader
from pydantic import EmailStr
from dotenv import load_dotenv
import os

# Cargamos el .env
load_dotenv()

# ... other imports from your existing code

frontend_url = os.getenv("FRONT_URL")

# Instanciar router Chats
auth_router = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"],
    responses={404: {"message": "No encontrado"}}
)

oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def create_email_template(user_name: str, verification_link: str, email: str, phone: str) -> str:
    # Load the Jinja2 environment, specifying the template folder
    env = Environment(loader=PackageLoader('main', 'templates'))  # Replace 'app' with your package name

    # Get the template object
    template = env.get_template("email_perso.html")  # Replace "nombreplantilla.html" with your actual template name

    # Render the template with the provided arguments
    return template.render(nombre_cliente=user_name, enlace_web=verification_link, correo=email, telefono=phone)


async def send_welcome_email(user: UserAddDTO, verification_link: str):
    try:
        contra = user.username[0].upper() + user.phone
        # Render the HTML content using the create_email_template function
        html_content = create_email_template(user.username, verification_link, user.email, contra)

        message = MessageSchema(
            subject="Bienvenido a la personalización de Tira de Papel",
            recipients=[user.email],
            template_body=html_content,
            subtype=MessageType.html,
        )

        fm = FastMail(conf)
        await fm.send_message(message)

    except Exception as e:
        # Handle potential errors during email sending gracefully (log the error, retry, etc.)
        print(f"Error sending email: {e}")

# Petición POST "/api/v1/auth/register"
# En el endpoint /register (En el caso local, http://localhost:8000/api/v1/auth/register)
# se ejecutará la función register si la petición es de tipo post.
# Registraremos un usuario en la bbdd.
# TODO Hacer que verifique el token
@auth_router.post("/register", response_model=UserDTO, status_code=status.HTTP_201_CREATED)
async def register(user: UserAddDTO, db: Session=Depends(get_db)):
    try:
        
        user = register_user(user, db)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El usuario ya existe")   
    await send_welcome_email(user, frontend_url)
    return user; 
    

# En el endpoint /login (En el caso local, http://localhost:8000/api/v1/auth/login)
# se ejecutará la función login si la petición es de tipo post.
# Recibiremos un usuario y una contraseña y verificaremos en la bbdd si los datos son correctos,
# devolviendo un token como respuesta.
@auth_router.post("/login", response_model=JSONResp)
async def login(form: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(get_db)):
    return check_login(form, db)


# En el endpoint /me (En el caso local, http://localhost:8000/api/v1/auth/me)
# se ejecutará la función me, que mostrará los datos del usuario logueado.
@auth_router.get("/me", response_model=UserDTO)
async def me(db: Session=Depends(get_db), token: str = Depends(oauth2)):
    return current_user(db, token)
