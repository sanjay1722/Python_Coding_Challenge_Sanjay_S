import pyodbc
from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_db_connection():
        conn_str = DBPropertyUtil.get_connection_string()
        return pyodbc.connect(conn_str)
