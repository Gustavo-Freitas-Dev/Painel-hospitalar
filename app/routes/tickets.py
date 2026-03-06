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