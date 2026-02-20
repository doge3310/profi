from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from db_init import VendMachine, Modem, VendModel, Employer, Role, EmployerStatus, Fix, Operator
from playhouse.shortcuts import model_to_dict
from pydantic import BaseModel


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*"
)


class Ta(BaseModel):
    name: str
    firm: str
    model: str
    status: str
    adress: str
    place: str
    coordinates: str
    ser_num: str
    work_time: str
    time_zone: str
    product_matrix: str
    krit_sample: str
    push_sample: str
    client: str
    manager: str
    enginer: str
    operator: str
    pay_system: str
    service_card: str
    incas_card: str
    download_card: str
    kit_id: str
    service_prior: str
    modem: str


@app.get("/get")
def machine_get():
    machine = VendMachine.select()
    json = {}

    for index, item in enumerate(machine):
        modem = Modem.get_by_id(item.modem)
        model = VendModel.get_by_id(item.model)
        operator = Operator.get_by_id(item.operator)

        json[index] = {
            "id": item.id,
            "name": item.name,
            "model": model.name,
            "firm": item.firm,
            "modem": modem.name,
            "company": item.firm,
            "adress": item.adress,
            "next_fix_date": item.next_fix_date,
            "place": item.place,
            "invent_num": item.invent_num,
            "operator": operator.name,
            "load": modem.load,
            "money": item.money,
            "date_expluatation": item.date_expluatation}

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


@app.get("/user/{email}")
def user_get(email):
    employer = Employer.get_or_none(email=email)
    employer = model_to_dict(employer)
    employer["role"] = employer["role"]["name"]
    employer["status"] = employer["status"]["name"]

    return employer


@app.post("/machine_insert")
def machine_insert(ta: Ta):
    VendMachine.get_or_create(
            name=ta.name,
            firm=ta.firm,
            model=ta.model,
            status=ta.status,
            adress=ta.adress,
            place=ta.place,
            coordinates=ta.coordinates,
            ser_num=ta.ser_num,
            work_time=ta.work_time,
            time_zone=ta.time_zone,
            product_matrix=ta.product_matrix,
            krit_sample=ta.krit_sample,
            push_sample=ta.push_sample,
            client=ta.client,
            manager=ta.manager,
            enginer=ta.enginer,
            operator=ta.operator,
            pay_system=ta.pay_system,
            service_card=ta.service_card,
            incas_card=ta.incas_card,
            download_card=ta.download_card,
            kit_id=ta.kit_id,
            service_prior=ta.service_prior,
            modem=ta.modem)


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
