from sqlalchemy import create_engine
import psycopg2
from sqlalchemy import text

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

    def get_companies(self):
        return self.db.execute(self.__scripts["select"]).fetchall()
    
    def get_company_by_id(self, id):
        return self.db.execute(self.__scripts["select by id"], select_id = id).fetchall()
    
    def get_active_companies(self):
        return self.db.execute(self.__scripts["select only active"]).fetchall()
    
    def delete_company(self, id):
        self.db.execute(self.__scripts["delete by id"], id_to_delete = id)

    def get_deleted_company(self, id):
        return self.db.execute(self.__scripts["get deleted"], deleted_id = id)

    def create_company(self, new_name, description):
        self.db.execute(self.__scripts["insert new"], new_name = new_name, description = description)

    def get_max_id(self):
       return  self.db.execute(self.__scripts["get max id"]).fetchall()[0][0]
        