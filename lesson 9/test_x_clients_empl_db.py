import requests 
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

#1.получение списка сотрудников созданной компании
def test_get_employees_empty_company():
# создаем компанию через БД
    db.create_company(name, description)
    max_id = db.get_max_id()
# получаем количество сотрудников через апи
    result_api = api_employee.get_employee_list(max_id)
# получаем количество сотрудников через db
    result_db = db_empl.get_employees(max_id)
# удаляем компанию
    db.delete_company(max_id)
# проверяем, что сотрудников нет
    len_result_api = len(result_api)
    len_result_db = len(result_db)
    
    assert len_result_api == len_result_db == 0
    

#2.1. добавление сотрудника (все поля заполнены)
def test_add_employee_valid():
    #создаем компанию
    db.create_company(name, description)
    max_id = db.get_max_id()

    # получить количество сотрудников
    result_db_before = db_empl.get_employees(max_id)
    # проверяем, что сотрудников нет
    len_before = len(result_db_before)

    # добавить нового сотрудника
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

    # получить количество сотрудников
    result_db_after = db_empl.get_employees(max_id)
    
    # получаем макс. id сотрудников из БД
    max_id_employee = db_empl.get_max_id_employee()

    # удаляем компанию
    db_empl.delete_employee(new_id)
    db.delete_company(max_id)
    len_after = len(result_db_after)

    # проверить, что их +1
    assert len_after - len_before == 1

    # проверить, что id последнего сотрудника в списке равен ответу из шага по созданию
    assert new_id == max_id_employee

#2.2. добавление сотрудника (обязательные поля не заполнены)
def test_add_employee_no_valid():
    #создаем компанию
    db.create_company(name, description)
    max_id = db.get_max_id()

    # добавить нового сотрудника
    
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
    
    db.delete_company(max_id)
    assert result["statusCode"] == 400
    assert result["message"] == [
        "firstName should not be empty",
        "lastName should not be empty"
    ]

#2.3. добавление сотрудника (не указан ID компании)
def test_add_employee_no_id_comp():
    #создаем компанию
    db.create_company(name, description)
    max_id = db.get_max_id()

    # добавить нового сотрудника
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
    db.delete_company(max_id)
    assert result["statusCode"] == 400
    

#3.получить сотрудника по ID
def test_get_employee():
    #создаем компанию
    db.create_company(name, description)
    max_id = db.get_max_id()

    #добавить нового сотрудника
        
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone = fake.msisdn()
    company_id = max_id
    db_empl.create_employee(first_name, last_name, phone, company_id)

    new_id = db_empl.get_max_id_employee()   
    
    #получить сотрудника по ID
    new_employee = api_employee.get_employee(new_id)
    db_empl.delete_employee(new_id)
    db.delete_company(max_id)

    assert new_employee["id"] == new_id
    assert new_employee["firstName"] == first_name
    assert new_employee["lastName"] == last_name
    assert new_employee["companyId"] == company_id
    

#4.редактирование сотрудника
def test_edit_employee():
    #создаем компанию
    db.create_company(name, description)
    max_id = db.get_max_id()

    #добавить нового сотрудника
        
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone = fake.msisdn()
    company_id = max_id
    db_empl.create_employee(first_name, last_name, phone, company_id)

    new_id = db_empl.get_max_id_employee()  

    #редактируем сотрудника
    new_lastname = "Петров"
    new_email = "test@mail.com"
    new_url = "www.petrov.com"
    new_phone = "79232323"
    new_isActive = True
    edited = api_employee.edit_employee(new_id, new_lastname, new_email, new_url, new_phone, new_isActive)

    db_empl.delete_employee(new_id)
    db.delete_company(max_id)
    
    assert edited["id"] == new_id
    assert edited["email"] == new_email
    assert edited["url"] == new_url
    assert edited["isActive"] == new_isActive


#5.удаление сотрудника
def test_delete_employee():
    #создаем компанию
    db.create_company(name, description)
    max_id = db.get_max_id()

    #добавить нового сотрудника
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone = fake.msisdn()
    company_id = max_id
    db_empl.create_employee(first_name, last_name, phone, company_id)

    #ищем сотрудника по id
    new_id = db_empl.get_max_id_employee()
    
    #удаляем сотрудника
    db_empl.delete_employee(new_id)
    #ищем сотрудника по id через api
    result = api_employee.get_employee(new_id)
    db.delete_company(max_id)
    
    #судя по сваггеру должно быть так, но при выполнении теста ошибка
    assert result["statusCode"] == 404
