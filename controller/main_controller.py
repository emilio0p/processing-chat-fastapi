from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/main",
    tags=["main"],
    responses={404: {"message": "Not found"}}
)

@router.get("/")
async def index():
    return "Hello FastAPI"


@router.get("/admin")
async def admin(name: str):
    if(name):
        return f"Hello {name}"
    
@router.get("/{name:str}")
async def user_name(name:str):
    return f"Hello {name}"