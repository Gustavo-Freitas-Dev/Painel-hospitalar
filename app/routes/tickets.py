from fastapi import APIRouter

router = APIRouter()

tickets = []
ticket_counter = 1

@router.post("/tickets")
def create_ticket():
    global ticket_counter

    ticket_number = f"A{ticket_counter:03}"

    ticket = {
        "ticket_number": ticket_number,
        "status": "waiting"
    }

    tickets.append(ticket)

    ticket_counter += 1

    return ticket

@router.get("/queue")
def get_queue():
    return tickets

@router.post("/tickets/call-next")
def call_next_ticket():
    if not tickets:
        return {"message": "Nenhum paciente na fila"}

    next_ticket = tickets.pop(0)

    return {
        "message": "Próximo paciente chamado",
        "ticket": next_ticket
    }