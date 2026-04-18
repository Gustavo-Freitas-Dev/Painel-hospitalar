from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional

class Endereco(BaseModel):
    rua: str
    numero: str
    cidade: str
    estado: str
    cep: str = Field(..., min_length=8, max_length=8)

class DadosMedicos(BaseModel):
    tipo_sanguineo: Optional[str] = None
    alergias: Optional[str] = None
    observacoes: Optional[str] = None

class CriarPaciente(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100)
    idade: int = Field(..., gt=0, lt=130)
    cpf: str = Field(..., min_length=11, max_length=11)
    email: Optional[EmailStr] = None
    telefone: str = Field(..., min_length=10, max_length=11)
    data_nascimento: date

    endereco: Endereco
    dados_medicos: Optional[DadosMedicos] = None