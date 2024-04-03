import requests 
import allure
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable
from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable
from faker import Faker

fake = Faker()

url = "https://x-clients-be.onrender.com"
db_empl = EmployeeTable("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")
db = CompanyTable("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")
api_company = CompanyApi(url)
api_employee = EmployeeApi(url)

name = fake.company()
description = 'New company'

@allure.epic("Сотрудники")

#1
@allure.title("Получение списка сотрудников созданной компании")
@allure.description("Создаем компанию и проверяем, что сотрудников в ней нет")
@allure.feature("READ")
@allure.severity("blocker")
def test_get_employees_empty_company():
    db.create_company(name, description)
    max_id = db.get_max_id()
    result_api = api_employee.get_employee_list(max_id)
    result_db = db_empl.get_employees(max_id)
    
    with allure.step("Проверить, что сотрудников нет"):
        len_result_api = len(result_api)
        len_result_db = len(result_db)
        
        assert len_result_api == len_result_db == 0
    db.delete_company(max_id)

#2.1
@allure.title("Добавление сотрудника (все поля заполнены)")
@allure.description("Добавление сотрудника, данные - валидные, позитивная проверка")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_add_employee_valid():
    db.create_company(name, description)
    max_id = db.get_max_id()

    result_db_before = db_empl.get_employees(max_id)
    len_before = len(result_db_before)

    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.first_name()
    companyId = max_id
    email = fake.ascii_email()
    url_ = fake.url()
    phone = fake.msisdn()
    birthdate = fake.date()
    isActive = True
    result = api_employee.create_employee(firstName, lastName, middleName, companyId, email, url_, phone, birthdate, isActive)
    new_id = result['id']

    result_db_after = db_empl.get_employees(max_id)
    max_id_employee = db_empl.get_max_id_employee()
    len_after = len(result_db_after)

    with allure.step("Проверить, что сотрудников увеличилось на 1"):
        assert len_after - len_before == 1

    with allure.step("Проверить, что id последнего сотрудника в списке равен ответу из шага 2"):
        assert new_id == max_id_employee

    db_empl.delete_employee(new_id)
    db.delete_company(max_id)

#2.2
@allure.title("Добавление сотрудника (обязательные поля не заполнены)")
@allure.description("Добавление сотрудника, негативная проверка")
@allure.feature("CREATE")
@allure.severity("normal")
def test_add_employee_no_valid():
    db.create_company(name, description)
    max_id = db.get_max_id()

    firstName = ""
    lastName = ""
    middleName = fake.first_name()
    companyId = max_id
    email = fake.ascii_email()
    url = fake.url()
    phone = fake.msisdn()
    birthdate = fake.date()
    isActive = ""
    result = api_employee.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    
    with allure.step("Проверить, что сотрудника добавить не удалось: статус-код 400, ошибка"):
        assert result["statusCode"] == 400
        assert result["message"] == [
            "firstName should not be empty",
            "lastName should not be empty"
        ]
    db.delete_company(max_id)

#2.3
@allure.title("Добавление сотрудника (не указан ID компании)")
@allure.description("Добавление сотрудника, негативная проверка")
@allure.feature("CREATE")
@allure.severity("normal")
def test_add_employee_no_id_comp():
    db.create_company(name, description)
    max_id = db.get_max_id()

    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.first_name()
    companyId = ""
    email = fake.ascii_email()
    url = fake.url()
    phone = fake.msisdn()
    birthdate = fake.date()
    isActive = True
    result = api_employee.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    
    with allure.step("Проверить, что сотрудника добавить не удалось: статус-код 400, ошибка"):
        assert result["statusCode"] == 400

    db.delete_company(max_id)
    

#3
@allure.title("Получение сотрудника по ID")
@allure.description("Получение сотрудника по ID")
@allure.feature("READ")
@allure.severity("critical")
def test_get_employee():
    db.create_company(name, description)
    max_id = db.get_max_id()

    first_name = fake.first_name()
    last_name = fake.last_name()
    phone = fake.msisdn()
    company_id = max_id
    db_empl.create_employee(first_name, last_name, phone, company_id)
    new_id = db_empl.get_max_id_employee()   
    
    new_employee = api_employee.get_employee(new_id)
    
    with allure.step("Проверить, что данные сотрудника корректные (соответствуют данным добавленного выше сотрудника)"):
        assert new_employee["id"] == new_id
        assert new_employee["firstName"] == first_name
        assert new_employee["lastName"] == last_name
        assert new_employee["companyId"] == company_id
    
    db_empl.delete_employee(new_id)
    db.delete_company(max_id)

#4
@allure.title("Редактирование сотрудника")
@allure.description("Редактирование данных сотрудника: фамилии, эл. почты, url, телефона, статуса")
@allure.feature("UPDATE")
@allure.severity("critical")
def test_edit_employee():
    db.create_company(name, description)
    max_id = db.get_max_id()

    first_name = fake.first_name()
    last_name = fake.last_name()
    phone = fake.msisdn()
    company_id = max_id
    db_empl.create_employee(first_name, last_name, phone, company_id)

    new_id = db_empl.get_max_id_employee()  

    new_lastname = "Петров"
    new_email = "test@mail.com"
    new_url = "www.petrov.com"
    new_phone = "79232323"
    new_isActive = True
    edited = api_employee.edit_employee(new_id, new_lastname, new_email, new_url, new_phone, new_isActive)

    with allure.step("Проверить, что данные сотрудника отредактированы"):
        assert edited["id"] == new_id
        assert edited["email"] == new_email
        assert edited["url"] == new_url
        assert edited["isActive"] == new_isActive

    db_empl.delete_employee(new_id)
    db.delete_company(max_id)

#5
@allure.title("Удаление сотрудника")
@allure.description("Удаление сотрудника по id")
@allure.feature("DELETE")
@allure.severity("critical")
def test_delete_employee():
    db.create_company(name, description)
    max_id = db.get_max_id()

    first_name = fake.first_name()
    last_name = fake.last_name()
    phone = fake.msisdn()
    company_id = max_id
    db_empl.create_employee(first_name, last_name, phone, company_id)

    new_id = db_empl.get_max_id_employee()
    
    db_empl.delete_employee(new_id)
    
    with allure.step("Проверить, что такого сотрудника нет (по id)"):
        result = api_employee.get_employee(new_id)
        assert result == "Not Found"
    
    db.delete_company(max_id)