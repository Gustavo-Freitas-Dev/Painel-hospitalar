from fastapi import APIRouter, HTTPException
from app.schemas.pacientes_schema import CriarPaciente

router = APIRouter(prefix='/pacientes', tags=['Pacientes'])

pacientes = []
contador_pacientes = 1


@router.post("/",
    summary='Cria um novo paciente',
    description='Essa rota adiciona um novo paciente a fila de espera.'
)
def criar_paciente(dados: CriarPaciente):
    global contador_pacientes

    novo_paciente = {
        "id": contador_pacientes,
        "nome": dados.nome,
        "idade": dados.idade,
        "cpf": dados.cpf,
        "email": dados.email,
        "telefone": dados.telefone,
        "data_nascimento": dados.data_nascimento,

        "endereco": {
            "rua": dados.endereco.rua,
            "numero": dados.endereco.numero,
            "cidade": dados.endereco.cidade,
            "estado": dados.endereco.estado,
            "cep": dados.endereco.cep
        },

        "dados_medicos": dados.dados_medicos
    }


    pacientes.append(novo_paciente)
    contador_pacientes += 1

    return novo_paciente


@router.get("/",
    summary='Lista os pacientes em espera',
    description='Essa rota lista todos os pacientes que estão aguardando atendimento.'
)
def listar_pacientes():
    return pacientes

@router.put(
    '/{id}',
    summary='Atualiza o cadastro de um paciente',
    description='Atualiza o cadastro de um paciente no banco de dados.'
)
def atualizar_paciente(id: int, dados: CriarPaciente):

    for paciente in pacientes:
        if paciente["id"] == id:

            # Converte o objeto Pydantic em dict, pega só os campos enviados na requisição
            # e atualiza o dicionário "paciente" sem apagar os outros dados
            paciente.update(dados.model_dump(exclude_unset=True))

            return paciente

    raise HTTPException(status_code=404, detail="Paciente não encontrado")