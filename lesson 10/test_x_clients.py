import requests 
import allure
from CompanyApi import CompanyApi

api = CompanyApi("https://x-clients-be.onrender.com")

@allure.story("Получение списка компаний")
@allure.title("Получение полного списка компаний")
@allure.description("Получение списка всех компаний")
@allure.severity("blocker")
def test_get_companies():
    body = api.get_company_list()
    with allure.step("Проверить, что список компаний больше 0"):
        assert len(body) > 0
    #assert resp.status_code == 200
    
@allure.story("Получение списка компаний")
@allure.title("Получение списка активных компаний")
@allure.description("Получение списка компаний с параметром active = True")
@allure.feature("READ")
@allure.severity("normal")
def test_get_active_companies():
    full_list = api.get_company_list()
         
    #my_params = {'active': 'true'}
    #resp = requests.get(base_url+'/company?', params=my_params)
    #или можно сразу в url передать resp = requests.get(base_url+'/company?', params={'active': 'true'})
    with allure.step("Получить отфильтрованный список компаний (статус - активный)"):
        filtered_list = api.get_company_list(params_to_add={'active': 'true'})
    with allure.step("Проверить, что полный список компаний больше отфильтрованного по активному статусу"):
        assert len(full_list) > len(filtered_list)

@allure.story("Добавление компании")
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
    #можно убрать названия параметров, так как они передаются в парильном порядке result = create_company(name, descr)
    new_id = result["id"]
    body = api.get_company_list()
    len_after = len(body)
    
    with allure.step("Проверить, что список компаний ПОСЛЕ больше списка компаний ДО"):
        assert len_after - len_before == 1

    with allure.step("Проверить название и описание последней компании"):
        assert body[-1]["name"] == name
        assert body[-1]["description"] == descr
    
    with allure.step("Проверить, что id последней компании в списке равен ответу из шага 2"):
        assert body[-1]["id"] == new_id

@allure.story("Получение компании по ID")
@allure.title("Получение компании по ID")
@allure.description("Получение компании по ID")
@allure.feature("READ")
@allure.severity("critical")
def test_get_one_company():
    name = "VS Code"
    descr = ''
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_company = api.get_company(new_id)
    with allure.step("Проверить, что данные полученной по id компании совпадают с данными созданной выше компании"):
        assert new_company["id"] == new_id
        assert new_company["name"] == name
        assert new_company["description"] == descr
        assert new_company["isActive"] == True

@allure.story("Редактирование компании")
@allure.title("Редактирование компании")
@allure.description("Редактирование данных компании: названия, описания и статуса")
@allure.feature("UPDATE")
@allure.severity("critical")
def test_edit():
    name = "Company"
    descr = ''
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_name = "UpDATED"
    new_descr = "__upd__"
    edited = api.edit_company(new_id, new_name, new_descr)
    
    with allure.step("Проверить, что данные компании отредактированы"):
        assert edited["id"] == new_id
        assert edited["name"] == new_name
        assert edited["description"] == new_descr
        assert edited["isActive"] == True

@allure.story("Удаление компании")
@allure.title("Удаление компании")
@allure.description("Удаление компании по id")
@allure.feature("DELETE")
@allure.severity("critical")
def test_delete():
    name = "Company to be deleted"
    result = api.create_company(name)
    new_id = result["id"]

    delited = api.delete_company(new_id)
    with allure.step("Проверить, данные удаленной компании совпадают с данными созданной выше компании"):
        assert delited["id"] == new_id
        assert delited["name"] == name
        assert delited["description"] == ''
        assert delited["isActive"] == True

    with allure.step("Проверить, что id последнего элемента не равен созданному выше"):
        body = api.get_company_list()
        assert body[-1]["id"] != new_id

@allure.story("(Де)активация компании")
@allure.title("Деактивация компании")
@allure.description("Деактивация компании, status - false")
@allure.feature("UPDATE")
@allure.severity("normal")
def test_deactivate():
    name = "Company to be deactivated"
    result = api.create_company(name = name)
    new_id = result["id"]
    
    body = api.set_active_state(new_id, False)
    with allure.step("Проверить, что статус активности компании - false"):
        assert body["isActive"] == False

@allure.story("(Де)активация компании")
@allure.title("Деактивация и последующая активация компании")
@allure.description("Деактивация (status - false) и последующая активация компании (status - true)")
@allure.feature("UPDATE")
@allure.severity("minor")
def test_deactivate_and_activate_back():
    name = "Company to be deactivated"
    result = api.create_company(name = name)
    new_id = result["id"]
    
    api.set_active_state(new_id, False)
    body = api.set_active_state(new_id, True)
    with allure.step("Проверить, что статус активности компании - true"):
        assert body["isActive"] == True
