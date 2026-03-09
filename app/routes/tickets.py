from fastapi import APIRouter, HTTPException
from app.schemas.tickets_schemas import CriarTickets
from app.routes.pacientes import pacientes

router = APIRouter()

fila_tickets = []
contador_tickets = 1


@router.post("/tickets")
def criar_ticket(dados: CriarTickets):
    global contador_tickets

    paciente_encontrado = None

    for paciente in pacientes:
        if paciente["id"] == dados.id_paciente:
            paciente_encontrado = paciente
            break

    if not paciente_encontrado:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")

    ticket = {
        "numero": contador_tickets,
        "paciente": paciente_encontrado["nome"],
        "status": "aguardando"
    }

    fila_tickets.append(ticket)
    contador_tickets += 1

    return ticket


@router.get("/queue")
def ver_fila():
    return fila_tickets


@router.post("/tickets/call-next")
def chamar_proximo_ticket():
    if not fila_tickets:
        return {"mensagem": "Nenhum paciente na fila"}

    proximo_ticket = fila_tickets.pop(0)
    proximo_ticket["status"] = "chamado"

    return {
        "mensagem": "Próximo paciente chamado",
        "ticket": proximo_ticket
    }