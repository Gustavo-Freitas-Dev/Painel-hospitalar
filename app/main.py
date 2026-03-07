from fastapi import FastAPI
from app.routes.pacientes import router as rota_pacientes
from app.routes.tickets import router as rota_tickets

app = FastAPI()

app.include_router(rota_pacientes)
app.include_router(rota_tickets)

@app.get('/')
def home():
    return {'mensagem': 'Api do painel hospitalar está rodando'}