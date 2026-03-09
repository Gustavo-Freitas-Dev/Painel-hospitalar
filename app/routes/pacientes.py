from fastapi import APIRouter
from app.schemas.pacientes_schema import CriarPacientes

router = APIRouter()

pacientes = []
contador_pacientes = 1


@router.post("/pacientes")
def criar_paciente(paciente: CriarPacientes):
    global contador_pacientes

    paciente = {
        "id": contador_pacientes,
        "nome": paciente.nome,
        "idade": paciente.idade
    }

    pacientes.append(paciente)
    contador_pacientes += 1

    return paciente


@router.get("/pacientes")
def listar_pacientes():
    return pacientes