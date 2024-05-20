# FORM TYPE DTO

# Importaciones
from pydantic import BaseModel

#Desarrollamos la clase base del DTO, con los atributos comunes
class FormTypeBaseDTO(BaseModel):
    form_name: str

#Desarrollamos la clase DTO y la configuramos para poder mostrarla en lectura
class FormTypeDTO(FormTypeBaseDTO):
    form_id: int

    class Config:
        orm_mode = True