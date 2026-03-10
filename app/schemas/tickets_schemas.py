from pydantic import BaseModel
from enum import Enum

class NivelUrgencia(str, Enum):
   baixa = 'baixa'
   media = 'media'
   alta = 'alta'
   emergencia = 'emergencia'

class CriarTickets(BaseModel):
   id_paciente: int
   urgencia: NivelUrgencia