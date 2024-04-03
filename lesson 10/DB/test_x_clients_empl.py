import allure
import requests 
from CompanyApi import CompanyApi
from EmployeeApi import EmployeeApi
from faker import Faker
fake = Faker()

url = "https://x-clients-be.onrender.com"

api_company = CompanyApi(url)
api_employee = EmployeeApi(url)

#1
@allure.story("Получение списка сотрудников компании")
@allure.title("Получение списка сотрудников созданной компании")
@allure.description("Создаем компанию и проверяем, что сотрудников в ней нет")
@allure.feature("READ")
@allure.severity("blocker")
def test_get_employees_empty_company():
    
    name = fake.company()
    descr = ''
    result = api_company.create_company(name, descr)
    company_id = result["id"]

    body = api_employee.get_employee_list(company_id)
    with allure.step("Проверить, что сотрудников нет"):
        len_before = len(body)
        assert len_before == 0

#2.1
@allure.story("Добавление сотрудника")
@allure.title("Добавление сотрудника (все поля заполнены)")
@allure.description("Добавление сотрудника, данные - валидные, позитивная проверка")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_add_employee_valid():
    
    name = fake.company()
    descr = ''
    result = api_company.create_company(name, descr)
    company_id = result["id"]

    body = api_employee.get_employee_list(company_id)
    
    len_before = len(body)

    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.first_name()
    companyId = company_id
    email = fake.ascii_email()
    url = fake.url()
    phone = fake.msisdn()
    birthdate = fake.date()
    isActive = True
    result = api_employee.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    new_id = result['id']

    body = api_employee.get_employee_list(company_id)
    len_after = len(body)
    
    with allure.step("Проверить, что сотрудников увеличилось на 1"):
        assert len_after - len_before == 1

    with allure.step("Проверить, что id последнего сотрудника в списке равен ответу из шага 2"):
        assert body[-1]["id"] == new_id

#2.2
@allure.story("Добавление сотрудника")
@allure.title("Добавление сотрудника (обязательные поля не заполнены)")
@allure.description("Добавление сотрудника, негативная проверка")
@allure.feature("CREATE")
@allure.severity("normal")
def test_add_employee_no_valid():
    
    name = fake.company()
    descr = ''
    result = api_company.create_company(name, descr)
    company_id = result["id"]

    firstName = ""
    lastName = ""
    middleName = fake.first_name()
    companyId = company_id
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

#2.3
@allure.story("Добавление сотрудника")
@allure.title("Добавление сотрудника (не указан ID компании)")
@allure.description("Добавление сотрудника, негативная проверка")
@allure.feature("CREATE")
@allure.severity("normal")
def test_add_employee_no_id_comp():
    
    name = fake.company()
    descr = ''
    result = api_company.create_company(name, descr)
    company_id = result["id"]

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
    
    with allure.step("Проверить, что сотрудника добавить не удалось: статус-код 400"):
        assert result["statusCode"] == 400
    

#3
@allure.story("Получение сотрудника по ID")
@allure.title("Получение сотрудника по ID")
@allure.description("Получение сотрудника по ID")
@allure.feature("READ")
@allure.severity("critical")
def test_get_employee():
    
    name = fake.company()
    descr = ''
    result = api_company.create_company(name, descr)
    company_id = result["id"]

    
    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.first_name()
    companyId = company_id
    email = fake.ascii_email()
    url = fake.url()
    phone = fake.msisdn()
    birthdate = fake.date()
    isActive = True
    result = api_employee.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    new_id = result["id"]
    
    new_employee = api_employee.get_employee(new_id)

    with allure.step("Проверить, что данные сотрудника корректные (соответствуют данным добавленного выше сотрудника)"):
        assert new_employee["id"] == new_id
        assert new_employee["firstName"] == firstName
        assert new_employee["lastName"] == lastName
        assert new_employee["companyId"] == companyId
        assert new_employee["isActive"] == isActive

#4
@allure.story("Редактирование сотрудника")
@allure.title("Редактирование сотрудника")
@allure.description("Редактирование данных сотрудника: фамилии, эл. почты, url, телефона, статуса")
@allure.feature("UPDATE")
@allure.severity("critical")
def test_edit_employee():
    
    name = fake.company()
    descr = ''
    result = api_company.create_company(name, descr)
    company_id = result["id"]

    
    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.first_name()
    companyId = company_id
    email = fake.ascii_email()
    url = fake.url()
    phone = fake.msisdn()
    birthdate = fake.date()
    isActive = True
    result = api_employee.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    new_id = result["id"]

    
    new_lastname = "Петров"
    new_email = "test@mail.com"
    new_url = "www.petrov.com"
    new_phone = "79232323"
    new_isActive = True
    edited = api_employee.edit_employee(new_id, new_lastname, new_email, new_url, new_phone, isActive)
    
    with allure.step("Проверить, что данные сотрудника отредактированы"):
        assert edited["id"] == new_id
        assert edited["email"] == new_email
        assert edited["url"] == new_url
        assert edited["isActive"] == new_isActive


"""
#Если нам нужно поработать с компанией по ID (не создавая каждый раз новую)

# указываем ID компании
company_id = 431

def test_get_employees():
    # получить количество сотрудников
    body = api_employee.get_employee_list(company_id)
    assert len(body) > 0

def test_add_employee_2():
    # получить количество сотрудников
    body = api_employee.get_employee_list(company_id)
    len_before = len(body)

    # добавить нового сотрудника
    id = fake.random_int()
    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.first_name()
    companyId = company_id
    email = fake.ascii_email()
    url = fake.url()
    phone = fake.msisdn()
    birthdate = fake.date()
    isActive = True
    result = api_employee.create_employee(id, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    new_id = result["id"]

    # получить количество сотрудников
    body = api_employee.get_employee_list(company_id)
    len_after = len(body)
    
    # проверить, что их +1
    assert len_after - len_before == 1

    # проверить, что id последнего сотрудника в списке равен ответу из шага 2
    assert body[-1]["id"] == new_id


def test_get_employee_2():
    # добавить нового сотрудника
    id = fake.random_int()
    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.first_name()
    companyId = company_id
    email = fake.ascii_email()
    url = fake.url()
    phone = fake.msisdn()
    birthdate = fake.date()
    isActive = True
    result = api_employee.create_employee(id, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    new_id = result["id"]
    #получить сотрудника по ID
    new_employee = api_employee.get_employee(new_id)

    assert new_employee["id"] == new_id
    assert new_employee["firstName"] == firstName
    assert new_employee["lastName"] == lastName
    assert new_employee["companyId"] == companyId
    assert new_employee["isActive"] == isActive

#4.редактирование сотрудника
def test_edit_employee_2():
    # добавить нового сотрудника
    id = fake.random_int()
    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.first_name()
    companyId = company_id
    email = fake.ascii_email()
    url = fake.url()
    phone = fake.msisdn()
    birthdate = fake.date()
    isActive = True
    
    result = api_employee.create_employee(id, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    new_id = result["id"]

    #редактируем сотрудника
    new_lastname = "Петров"
    new_email = "test@mail.com"
    new_url = "www.petrov.com"
    new_phone = "79232323"
    new_isActive = True
    edited = api_employee.edit_employee(new_id, new_lastname, new_email, new_url, new_phone, isActive)
    assert edited["id"] == new_id
    assert edited["email"] == new_email
    assert edited["url"] == new_url
    assert edited["isActive"] == new_isActive

"""