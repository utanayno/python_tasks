from sqlalchemy import create_engine
import psycopg2
from sqlalchemy import text

class EmployeeTable:
    
    __scripts = {
        "select": text("select * from employee where \"company_id\" = :company_id"),
        "select employee by id": text("select * from employee where id = :select_id"),
        "get max id employee" : text("select max(id) from employee"),
        "insert employee": text(
            """INSERT INTO employee (is_active, create_timestamp, change_timestamp, 
            first_name, last_name, phone, company_id) 
            VALUES (true, now(), now(), :first_name, :last_name, :phone, :company_id)""")

    }
    
    
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_employees(self, id):
        return self.db.execute(self.__scripts["select"], company_id = id).fetchall()
    
    def get_employee_by_id(self, id):
        return self.db.execute(self.__scripts["select employee by id"], select_id = id).fetchall()
    
    def create_employee(self, first_name, last_name, phone, company_id):
        self.db.execute(self.__scripts["insert employee"], first_name = first_name, last_name = last_name, phone=phone, company_id=company_id)

    def get_max_id_employee(self):
        return  self.db.execute(self.__scripts["get max id employee"]).fetchall()[0][0]

    
    
    
        