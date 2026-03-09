from pydantic import BaseModel

class CriarPacientes(BaseModel):
    nome: str
    idade: int