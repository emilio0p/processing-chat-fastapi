from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from controller.user_controller import user_router
from controller.chat_controller import chat_router
from controller.auth_controller import auth_router
from controller.message_controller import message_router

# Instancia FastAPI
app = FastAPI()

# Configurar CORS para FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(chat_router)
app.include_router(message_router)