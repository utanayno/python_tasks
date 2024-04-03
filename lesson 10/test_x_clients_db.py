import requests 
import allure
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable

api = CompanyApi("https://x-clients-be.onrender.com")
db = CompanyTable("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")

@allure.title("Получение полного списка компаний")
@allure.description("Получение списка всех компаний")
@allure.feature("READ")
@allure.severity("blocker")
def test_get_companies():
    api_result = api.get_company_list()
    db_result = db.get_companies()
    with allure.step("Проверить, что список компаний, полученных через БД и Api, равны"):
        assert len(api_result) == len(db_result)

@allure.title("Получение списка активных компаний")
@allure.description("Получение списка компаний с параметром active = True")
@allure.feature("READ")    
@allure.severity("normal")
def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={'active': 'true'})
    db_list = db.get_active_companies()
    with allure.step("Проверить, что список компаний, полученных через БД и Api, равны"):
        assert len(filtered_list) == len(db_list)

@allure.title("Добавление компании")
@allure.description("Добавление компании c именем и описанием")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_add_new():
    body = api.get_company_list()
    len_before = len(body)
    
    name = "Autotest"
    descr = "Descr"
    result = api.create_company(name = name, description = descr)
    #можно убрать названия параметров, так как они передаются в правильном порядке result = create_company(name, descr)
    new_id = result["id"]
    body = api.get_company_list()
    len_after = len(body)

    with allure.step("Проверить, что список ДО меньше списка ПОСЛЕ на 1"):
        assert len_after - len_before == 1
    
    with allure.step("Проверить, что поля новой компании корректно заполнены"):
    #body - список организаций, которые пришли через api, если id равен нашему, то делаем проверки
        for company in body:
            if company["id"] == new_id:
                # проверить название и описание последней компании
                assert company["name"] == name
                assert company["description"] == descr
    with allure.step("Проверить, id последней компании в списке равен ответу из шага 2"):
        assert company["id"] == new_id

    db.delete_company(new_id)

@allure.title("Получение компании по ID")
@allure.description("Получение компании по ID")
@allure.feature("READ")
@allure.severity("critical")
def test_get_one_company():
    name = 'SkyPro'
    description = 'New company'
    db.create_company(name, description)
    max_id = db.get_max_id()

    new_company = api.get_company(max_id)
    
    with allure.step("Проверить, что поля компании, полученные из БД и через API, совпадают"):
        assert new_company["id"] == max_id
        assert new_company["name"] == name
        assert new_company["description"] == description
        assert new_company["isActive"] == True
    
    db.delete_company(max_id)

@allure.title("Редактирование компании")
@allure.description("Редактирование данных компании: названия, описания и статуса")
@allure.feature("UPDATE")
@allure.severity("critical")
def test_edit():
    name = 'SkyPro'
    description = 'New company'
    db.create_company(name, description)
    max_id = db.get_max_id()

    new_name = "UpDATED"
    new_descr = "__upd__"
    edited = api.edit_company(max_id, new_name, new_descr)
    
    with allure.step("Проверить, что поля отредактированной компании заполнены корректно"):
        assert edited["id"] == max_id
        assert edited["name"] == new_name
        assert edited["description"] == new_descr
        assert edited["isActive"] == True

    db.delete_company(max_id)

@allure.title("Удаление компании")
@allure.description("Удаление компании по id")
@allure.feature("DELETE")
@allure.severity("critical")
def test_delete():
    name = 'SkyPro'
    description = 'New company'
    db.create_company(name, description)
    max_id = db.get_max_id()

    deleted = api.delete_company(max_id)
    
    with allure.step("Проверить, что поля удаленной компании заполнены корректно"):
        assert deleted["id"] == max_id
        assert deleted["name"] == name
        assert deleted["description"] == description
        assert deleted["isActive"] == True

    #проверить, что есть организация с таким id и deleted_at not null
    #rows = db.get_company_by_id(max_id)
    #assert len(rows) == 1

    #rows = api.get_company(max_id)
    #assert len(rows) == 0

    #проверить, что у удаленной компании deleted_at not null
    #deleted_db = db.get_deleted_company(max_id)
    #assert deleted_db[max_id] == deleted["id"]

@allure.feature("(Де)активация компании")
@allure.title("Деактивация компании")
@allure.description("Деактивация компании, status - false")
@allure.severity("normal")
def test_deactivate():
    name = 'SkyPro'
    description = 'New company'
    db.create_company(name, description)
    max_id = db.get_max_id()
    
    body = api.set_active_state(max_id, False)
    
    with allure.step("Проверить, что статус деактивированной компании - false"):
        assert body["isActive"] == False

    db.delete_company(max_id)

@allure.feature("(Де)активация компании")
@allure.title("Деактивация и активация компании")
@allure.description("Деактивация (status - false) и последующая активация компании (status - true)")
@allure.severity("minor")
def test_deactivate_and_activate_back():
    name = 'SkyPro'
    description = 'New company'
    db.create_company(name, description)
    max_id = db.get_max_id()
    
    api.set_active_state(max_id, False)
    body = api.set_active_state(max_id, True)
    
    with allure.step("Проверить, что статус активированной компании - true"):
        assert body["isActive"] == True

    db.delete_company(max_id)
