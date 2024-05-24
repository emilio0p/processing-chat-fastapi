# Importaciones
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from controller.user_controller import user_router
from controller.chat_controller import chat_router
from controller.auth_controller import auth_router

# Instancia FastAPI
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(chat_router)