from peewee import MySQLDatabase, Model, \
    AutoField, CharField, ForeignKeyField, \
    DateField, IntegerField, DateTimeField, SQL, TimeField
import pymysql
from pymysql import MySQLError
from datetime import date
from hasher import get_hash

password = "1234_8765"
user = "root"
host = "localhost"
port = 3306
db_name = "users_1"


def init():
    try:
        database_connect = pymysql.connect(user=user,
                                        password=password,
                                        host=host)

        with database_connect.cursor() as cursor:
            cursor.execute(f"create database if not exists {db_name}")

    except MySQLError as e:
        print(e)

    finally:
        if "database_connect" in locals() and database_connect:
            database_connect.close()


init()

db_connect = MySQLDatabase(db_name,
                           user=user,
                           password=password,
                           host=host,
                           port=port)


class Table(Model):
    class Meta:
        database = db_connect


class VendModel(Table):
    id = AutoField()
    name = CharField()


class VendStatus(Table):
    id = AutoField()
    name = CharField()


class Role(Table):
    id = AutoField()
    name = CharField()


class EmployerStatus(Table):
    id = AutoField()
    name = CharField()


class Employer(Table):
    id = AutoField()
    first_name = CharField()
    mid_name = CharField()
    last_name = CharField()
    password = CharField()
    email = CharField()
    phone = CharField()
    status = ForeignKeyField(EmployerStatus)
    role = ForeignKeyField(Role)


class KitOnline(Table):
    id = AutoField()
    name = CharField()


class Operator(Table):
    id = AutoField()
    name = CharField()
    rate = IntegerField()


class Modem(Table):
    id = AutoField()
    name = CharField()
    operator = ForeignKeyField(Operator)
    load = CharField()


class VendMachine(Table):
    id = AutoField()
    adress = CharField()
    place = CharField()
    coordinates = CharField()
    work_time = TimeField()
    time_zone = CharField()
    product_matrix = CharField()
    krit_sample = CharField()
    push_sample = CharField()
    client = ForeignKeyField(Employer)
    manager = ForeignKeyField(Employer)
    enginer = ForeignKeyField(Employer)
    operator = ForeignKeyField(Employer)
    pay_system = CharField()
    service_card = CharField()
    incas_card = CharField()
    download_card = CharField()
    kit_id = ForeignKeyField(KitOnline)
    service_prior = CharField()
    model = ForeignKeyField(VendModel)
    name = CharField()
    money = IntegerField()
    ser_num = CharField()
    invent_num = CharField()
    firm = CharField()
    modem = ForeignKeyField(Modem)
    date_expluatation = DateField()
    date_created = DateField(default="20.01.01")
    date_last_test = DateField()
    test_interval = IntegerField()
    resource = IntegerField(default=1)
    next_fix_date = DateField(default="99.01.01")
    fix_time = IntegerField(default=2)
    status = ForeignKeyField(VendStatus)
    create_country = CharField()
    invent_date = DateField(default="21.01.01")
    test_employer = ForeignKeyField(Employer, default=1)
    date_inserted = DateTimeField(default=date.today().strftime("%d.%m.%Y"))

    class Meta:
        dattim = date.today()
        constraints = [SQL("check (resource >= 0)"),
                       SQL("check (next_fix_date > date_inserted)"),
                       SQL("check (fix_time between 1 and 20)"),
                       SQL(f"check (invent_date between date_created and '{dattim}')")]


class Product(Table):
    id = AutoField()
    name = CharField()
    description = CharField()
    price = IntegerField()
    count = IntegerField()
    min_count = IntegerField()
    sale_tendency = CharField()


class Fix(Table):
    id = AutoField()
    machine = ForeignKeyField(VendMachine)
    fix_date = DateField()
    description = CharField()
    problem = CharField()
    employer = ForeignKeyField(Employer)


def main():
    test, _ = VendModel.get_or_create(
        name="test_model"
    )

    test, _ = VendStatus.get_or_create(
        name="work"
    )

    test, _ = Role.get_or_create(
        name="admin"
    )

    test, _ = EmployerStatus.get_or_create(
        name="active"
    )

    test, _ = Employer.get_or_create(
        email="test@",
        phone="678905",
        defaults={
            "first_name": "sdfghdd",
            "mid_name": "dfghj",
            "last_name": "dh",
            "role": 1,
            "password": get_hash("123"),
            "status": 1
        }
    )

    test, _ = KitOnline.get_or_create(
        name="1423"
    )

    test, _ = Operator.get_or_create(
        name="sdfgjil",
        rate="ghuio"
    )

    test, _ = Modem.get_or_create(
        name="sdfghuil",
        operator=1,
        load="1/20"
    )

    test, _ = VendMachine.get_or_create(
        adress="ул. Ленина, 1",
        place="Офис",
        coordinates="55.0, 37.0",
        work_time="08:00",
        time_zone="MSK",
        product_matrix="A1",
        krit_sample="S1",
        push_sample="P1",
        client=1,
        manager=1,
        enginer=1,
        operator=1,
        pay_system="Card",
        service_card="123",
        incas_card="456",
        download_card="789",
        kit_id=1,
        service_prior="Normal",
        model=1,
        name="Тестовый автомат",
        money=23456,
        ser_num="SN123",
        invent_num="INV123",
        firm="VendorCorp",
        modem=1,
        date_expluatation="21.01.01",
        date_created="20.01.01",
        date_last_test="21.02.01",
        test_interval=30,
        resource=100,
        next_fix_date="27.01.01",
        fix_time=10,
        status=1,
        create_country="RU",
        invent_date="21.01.01",
        test_employer=1
    )

    test, _ = VendMachine.get_or_create(
        adress="ул. Ленина, 1",
        place="Офис",
        coordinates="55.0, 37.0",
        work_time="08:00",
        time_zone="MSK",
        product_matrix="A1",
        krit_sample="S1",
        push_sample="P1",
        client=1,
        manager=1,
        enginer=1,
        operator=1,
        pay_system="Card",
        service_card="123",
        incas_card="456",
        download_card="789",
        kit_id=1,
        service_prior="Normal",
        model=1,
        name="Тестовый2 автомат",
        money=23456,
        ser_num="SN123",
        invent_num="INV123",
        firm="VendorCorp",
        modem=1,
        date_expluatation="21.01.01",
        date_created="20.01.01",
        date_last_test="21.02.01",
        test_interval=30,
        resource=100,
        next_fix_date="27.01.10",
        fix_time=10,
        status=1,
        create_country="RU",
        invent_date="21.01.01",
        test_employer=1
    )

    test, _ = Product.get_or_create(
        name="dfghs",
        defaults={
            "description": "sdfghsghsghf",
            "price": 12341,
            "count": 123,
            "min_count": 123,
            "sale_tendency": "dfghj"
        }
    )

    test, _ = Fix.get_or_create(
        machine=1,
        defaults={
            "description": "fghd;dfgh",
            "problem": "sndg",
            "employer": 1
        }
    )


if __name__ == "__main__":
    db_connect.create_tables([VendMachine,
                              VendStatus,
                              Role,
                              Employer,
                              VendModel,
                              Product,
                              Fix,
                              KitOnline,
                              Modem,
                              Operator,
                              EmployerStatus])
    main()
