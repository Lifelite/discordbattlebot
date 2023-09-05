import os
import MySQLdb
from dotenv import load_dotenv


class Database:

    @staticmethod
    def my_sql_connect():
        load_dotenv(override=True)
        connection = MySQLdb.connect(host=os.getenv("HOST"),
                                     user=os.getenv("USERNAME"),
                                     password=os.getenv("PASSWORD"),
                                     database=os.getenv("DATABASE"),
                                     autocommit=True,
                                     ssl_mode="VERIFY_IDENTITY",
                                     ssl={
                                         "ca": "C:/ca/cacert.pem"
                                     })
        db = connection
        return db


class Query(Database):

    def __init__(self):
        self.db = Database.my_sql_connect()
        self.connect = self.db.my_sql_connect()
        self.c = self.connect.cursor()

    def commit_toon(self, t_name, weapon, hp, mp, sp_move, t_type, t_user):
        self.c.execute(f"INSERT INTO toons (t_name, weapons, hp, mp, sp_move, t_type, t_user) "
                       f"VALUES ({t_name}, {weapon}, {hp}, {mp}, {sp_move}, {t_type}, {t_user});")


    def find_toon(self, user):
        self.c.execute("SELECT t_name, weapons, hp, mp, sp_move, t_type FROM toons \
        WHERE t_user = \"" + user + "\";")
        creds = self.c.fetchone()
        return creds

    def manual_query(self, sql):
        self.c.execute(sql)
