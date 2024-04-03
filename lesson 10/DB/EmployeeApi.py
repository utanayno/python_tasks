import requests
import allure
class EmployeeApi:
    """
    Класс представляет работу с сущностью Работника через API
    """

    def __init__(self, url):
        self.url = url

    @allure.step("Api. Получить токен авторизации для пользователя {user}:{password}")
    def get_token(self, user : str = 'bloom', password : str = 'fire-fairy') -> str:  # значения по умолчанию. Если ничего не указывать, то подставятся они. Если указать свои, то подставятся свои.
        """
            Метод на сохранение пользовательского токена
        """
        creds = {
            'username' : user,
            'password' : password
        }
    #авторизация
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]

    @allure.step("Api. Получить список сотрудников для компании {company}")
    def get_employee_list(self, company : str) -> list:
        resp = requests.get(self.url+'/employee?company='+ str(company))
        return resp.json()
    
    @allure.step("Api. Добавить сотрудника")
    def create_employee(self, firstName : str, lastName : str, middleName : str, companyId : str, email : str, url : str, phone : str, birthdate : str, isActive: bool) -> dict:
        """
            Метод на добавление сотрудника (все поля заполнены)
        """
        employee = {
            "firstName": firstName,
            "lastName": lastName,
            "middleName": middleName,
            "companyId": companyId,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": isActive
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url+'/employee', json=employee, headers=my_headers)
        return resp.json()
    
    @allure.step("Api. Получить сотрудника {id}")
    def get_employee(self, id: int) -> dict:
        """
            Метод на получение конкретного сотрудника
        """
        resp = requests.get(self.url+'/employee/'+ str(id))
        if resp.text:
            return resp.json()
        else:
            return "Not Found"
    
    @allure.step("Api. Редактировать сотрудника")
    def edit_employee(self, new_id : int, new_lastname : str, new_email : str, new_url : str, new_phone : str, isActive: bool) -> dict:
        """
            Метод на редактирование сотрудника
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        employee = {
                "lastName": new_lastname,
                "email": new_email,
                "url": new_url,
                "phone": new_phone,
                "isActive": isActive
                }
    

        resp = requests.patch(self.url+'/employee/'+ str(new_id), headers=my_headers, json=employee)
        return resp.json()