from sqlalchemy import create_engine
import psycopg2
import allure
from sqlalchemy import text

class EmployeeTable:
    
    __scripts = {
        "select": text("select * from employee where \"company_id\" = :company_id"),
        "select employee by id": text("select * from employee where id = :select_id"),
        "get max id employee" : text("select max(id) from employee"),
        "insert employee": text("INSERT INTO employee (is_active, create_timestamp, change_timestamp, first_name, last_name, phone, company_id) VALUES (true, now(), now(), :first_name, :last_name, :phone, :company_id)"),
        "delete by id" : text("delete from employee where id = :id_to_delete")

    }
    
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    @allure.step("БД. Получить список сотрудников для компании {id}")
    def get_employees(self, id : int) -> list:
        return self.db.execute(self.__scripts["select"], company_id = id).fetchall()
    
    @allure.step("БД. Получить сотрудника {id}")
    def get_employee_by_id(self, id : int) -> dict:
        return self.db.execute(self.__scripts["select employee by id"], select_id = id).fetchall()
    
    @allure.step("БД. Добавить сотрудника")
    def create_employee(self, first_name : str, last_name : str, phone : str, company_id: int):
        self.db.execute(self.__scripts["insert employee"], first_name = first_name, last_name = last_name, phone=phone, company_id=company_id)
    
    @allure.step("БД. Получить максимальный id сотрудника")
    def get_max_id_employee(self) -> int:
        return  self.db.execute(self.__scripts["get max id employee"]).fetchall()[0][0]
    
    @allure.step("БД. Удалить сотрудника {id}")
    def delete_employee(self, id : int):
        self.db.execute(self.__scripts["delete by id"], id_to_delete = id)

    """INSERT INTO employee (is_active, create_timestamp, change_timestamp, 
            first_name, last_name, phone, company_id) 
            VALUES (true, now(), now(), :first_name, :last_name, :phone, :company_id)"""
    
    
        