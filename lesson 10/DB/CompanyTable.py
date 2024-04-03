from sqlalchemy import create_engine
import psycopg2
from sqlalchemy import text
import allure

class CompanyTable:
    #скрипты для команд (для удобства)

    __scripts = {
        "select": "select * from company",
        "select by id": text("select * from company where id = :select_id"),
        "select only active" : "select * from company where \"is_active\" = true",
        "delete by id" : text("delete from company where id = :id_to_delete"),
        "get deleted" : text("select * from company where id = :deleted_id and \"deleted_at\" IS NOT NULL"),
        "insert new" : text("insert into company (\"name\", \"description\") values (:new_name, :description)"),
        "get max id" : "select max(id) from company"
    }
    
    
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
    
    @allure.step("БД. Получить список компаний")
    def get_companies(self):
        query = self.db.execute(self.__scripts["select"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()
   
    @allure.step("БД. Получить компанию по id {id}")
    def get_company_by_id(self, id : int) -> dict:
        return self.db.execute(self.__scripts["select by id"], select_id = id).fetchall()
    
    @allure.step("БД. Получить список активных компаний")
    def get_active_companies(self):
        return self.db.execute(self.__scripts["select only active"]).fetchall()
    
    @allure.step("БД. Удалить компанию {id}")
    def delete_company(self, id : int):
        self.db.execute(self.__scripts["delete by id"], id_to_delete = id)

    @allure.step("БД. Получить удаленную компанию {id}")
    def get_deleted_company(self, id : int) -> dict:
        return self.db.execute(self.__scripts["get deleted"], deleted_id = id)
    
    @allure.step("БД. Создать компанию c названием {new_name} и описанием {description}")
    def create_company(self, new_name : str, description: str) -> dict:
        self.db.execute(self.__scripts["insert new"], new_name = new_name, description = description)

    @allure.step("БД. Получить максимальный id компании")
    def get_max_id(self):
       return  self.db.execute(self.__scripts["get max id"]).fetchall()[0][0]
        