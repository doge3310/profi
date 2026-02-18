from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from db_init import VendMachine, Modem, VendModel, Employer, Role, EmployerStatus, Fix


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*"
)


@app.get("/get")
def machine_get():
    machine = VendMachine.select()
    json = {}

    for index, item in enumerate(machine):
        modem = Modem.get_by_id(item.modem)
        model = VendModel.get_by_id(item.model)

        json[index] = {
            "id": item.id,
            "name": item.name,
            "model": model.name,
            "modem": modem.name,
            "company": item.firm,
            "adress": item.adress,
            "next_fix_date": item.next_fix_date}

    return json


@app.get("/employers")
def employers_get():
    json = {}
    employers = Employer.select()

    for index, item in enumerate(employers):
        role = Role.get_by_id(item.role)
        status = EmployerStatus.get_by_id(item.status)
        json[index] = {
            "first_name": item.first_name,
            "last_name": item.last_name,
            "mid_name": item.mid_name,
            "email": item.email,
            "phone": item.phone,
            "role": role.name,
            "status": status.name}

    return json


@app.get("/fixes")
def get_fix():
    machines = Fix.select()
    json = {}

    for index, item in enumerate(machines):
        machine = VendMachine.get_by_id(item.machine)
        employer = Employer.get_by_id(item.employer)

        json[index] = {
            "machine": machine.id,
            "machine_serial": machine.ser_num,
            "description": item.description,
            "problem": item.problem,
            "employer": employer.email}

    return json


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
