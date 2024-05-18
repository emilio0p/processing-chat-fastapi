# Importaciones
from fastapi import APIRouter

# Instanciar router Main
router = APIRouter(
    prefix="/api/v1/main",
    tags=["main"],
    responses={404: {"message": "No encontrado"}}
)

# Petición GET "/"
@router.get("/")
async def index():
    return "Hello FastAPI"

# Petición GET "/admin"
@router.get("/admin")
async def admin(name: str):
    if(name):
        return f"Hello {name}"
    
# Petición GET "/name"
@router.get("/{name:str}")
async def user_name(name:str):
    return f"Hello {name}"