from fastapi import APIRouter

router = APIRouter()

patients = []

@router.post("/pacientes")
def create_patient(name: str):
    patient = {"name": name}
    patients.append(patient)
    return patient