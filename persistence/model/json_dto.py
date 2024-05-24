from pydantic import BaseModel

#Vamos a desarrollar el objeto de transferencia de datos

#Desarrollamos la clase base del DTO, con los atributos comunes
class JSONResp(BaseModel):
    access_token: str
    token_type: str
    
    class Config:
        orm_mode = True