import requests
class ToDoApi:

    def __init__(self, url):
        self.url = url

#https://todo-app-sky.herokuapp.com/

#Создание
    def add_task(self, title, status=''):
        task =  {
            "title": title,
            "completed": status
            }
        resp = requests.post(self.url, json=task)
        return resp.json()

#Переименование
    def edit(self, id, title):
        new_task =  {
            "title": title
            }

        resp = requests.patch(self.url+str(id), json=new_task)
        return resp.json()

#Удаление
    def delete_task(self, id):
        resp = requests.delete(self.url+str(id))
        return resp.json()

#Получение списка
    def get_list(self):
        resp = requests.get(self.url)
        return resp.json()

#Получение конкретной задачи из списка
    def get_task(self, id):
        resp = requests.get(self.url+str(id))
        return resp.json()

#Отметка задачи «Выполнена»
    def completed(self, id):
        task =  {
            "completed": True
            }

        resp = requests.patch(self.url+str(id), json=task)
        return resp.json()

#Снятие отметки «Выполнена»
    def uncompleted(self, id):
        task =  {
            "completed": False
            }

        resp = requests.patch(self.url+str(id), json=task)
        return resp.json()