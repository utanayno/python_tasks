import requests
class CompanyApi:

    def __init__(self, url):
        self.url = url

        #url указывается один раз (например на тестовом стенде, или на проде, и т.д.)

    #метод на получение списка компаний
    def get_company_list(self, params_to_add = None):                         #если параметров нет, то подставится None
        resp = requests.get(self.url+'/company', params=params_to_add)
        return resp.json()
    
    #метод на получение конкретной компании
    def get_company(self, id):
        resp = requests.get(self.url+'/company/'+ str(id))
        return resp.json()

    #метод на сохранение пользовательского токена
    def get_token(self, user = 'bloom', password = 'fire-fairy'):  # значения по умолчанию. Если ничего не указывать, то подставятся они. Если указать свои, то подставятся свои.
        creds = {
            'username' : user,
            'password' : password
        }
    #авторизация
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]

    #метод на создание компании
    def create_company(self, name, description=''):
        company = {
            "name" : name,
            "description" : description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url+'/company', json=company, headers=my_headers)
        return resp.json()
    
    #метод на редактирование компании
    def edit_company(self, new_id, new_name, new_descr):
        # когда вызовут метод, создастся словарь
        my_headers = {}
        # положи в словарь значения из метода, авторизуйся
        my_headers["x-client-token"] = self.get_token()

        company = {
            "name" : new_name,
            "description" : new_descr
        }

        resp = requests.patch(self.url+'/company/'+ str(new_id), headers=my_headers, json=company)
        return resp.json()
    
    def delete_company(self, id):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.get(self.url+'/company/delete/'+ str(id), headers=my_headers)
        return resp.json()
    
    def set_active_state(self, id, isActive):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url+'/company/status/'+ str(id), headers=my_headers, json={'isActive': isActive})
        return resp.json()
    
    

    
