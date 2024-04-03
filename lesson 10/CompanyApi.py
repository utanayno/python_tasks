import requests
import allure
class CompanyApi:
    """Класс представляет методы для работы с сервером приложения. Компании"""

    def __init__(self, url):
        self.url = url

        #url указывается один раз (например на тестовом стенде, или на проде, и т.д.)

    @allure.step("Api. Получить список компаний")
    def get_company_list(self, params_to_add = None) -> list:                         #если параметров нет, то подставится None
        resp = requests.get(self.url+'/company', params=params_to_add)
        return resp.json()
    
    @allure.step("Api. Получить конкретную компанию {id}")
    def get_company(self, id : int) -> dict:
        resp = requests.get(self.url+'/company/'+ str(id))
        return resp.json()

    @allure.step("Api. Получить токен авторизации для пользователя {user} : {password}")
    def get_token(self, user : str = 'bloom', password : str = 'fire-fairy') -> str:  # значения по умолчанию. Если ничего не указывать, то подставятся они. Если указать свои, то подставятся свои.
        creds = {
            'username' : user,
            'password' : password
        }
    #авторизация
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]

    @allure.step("Api. Создать компанию с названием {name} и описанием {description}")
    def create_company(self, name : str, description : str ='') -> str:
        company = {
            "name" : name,
            "description" : description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url+'/company', json=company, headers=my_headers)
        return resp.json()
    
    @allure.step("Api. Редактировать компанию {new_id}")
    def edit_company(self, new_id : int, new_name : str, new_descr : str) -> str:
        # когда вызовут метод, создастся словарь
        my_headers = {}
        # положи в словарь значения из метода, авторизуйся
        my_headers["x-client-token"] = self.get_token()

        company = {
            "name" : new_name,
            "description" : new_descr
        }

        resp = requests.patch(self.url+'/company/'+ str(new_id), headers = my_headers, json=company)
        return resp.json()
    
    @allure.step("Api. Удалить компанию {id}")
    def delete_company(self, id : int):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.get(self.url+'/company/delete/'+ str(id), headers=my_headers)
        return resp.json()
    
    @allure.step("Api. (Де)активировать компанию {id}")
    def set_active_state(self, id : int, isActive : bool) -> bool:
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url+'/company/status/'+ str(id), headers=my_headers, json={'isActive': isActive})
        return resp.json()
    
    

    
