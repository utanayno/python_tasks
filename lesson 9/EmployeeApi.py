import requests
class EmployeeApi:

    def __init__(self, url):
        self.url = url

    #метод на сохранение пользовательского токена
    def get_token(self, user = 'bloom', password = 'fire-fairy'):  # значения по умолчанию. Если ничего не указывать, то подставятся они. Если указать свои, то подставятся свои.
        creds = {
            'username' : user,
            'password' : password
        }
    #авторизация
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]

    #метод на получение списка сотрудников для компании
    def get_employee_list(self, company):
        resp = requests.get(self.url+'/employee?company='+ str(company))
        return resp.json()
    
    #метод на добавление сотрудника (все поля заполнены)
    def create_employee(self, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive):
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
    
     #метод на получение конкретного сотрудника
    def get_employee(self, id):
        resp = requests.get(self.url+'/employee/'+ str(id))
        return resp.json()
    
    #метод на редактирование сотрудника
    def edit_employee(self, new_id, new_lastname, new_email, new_url, new_phone, isActive):
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