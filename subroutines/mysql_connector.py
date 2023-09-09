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
        self.c = self.db.cursor()


    def commit_toon(self, t_name, weapon, hp, mp, sp_move, t_type, t_user):
        print(str(t_user))
        t_name = str(t_name)
        weapon = str(weapon)
        hp = str(hp)
        mp = str(mp)
        sp_move = str(sp_move.value)
        t_type = str(t_type)
        t_user = str(t_user)
        t_user = t_user.translate({ord(i): None for i in "' {}"})

        self.c.execute(f"""INSERT INTO toons(t_name, weapons, hp, mp, sp_move, t_type, t_user) \
                       VALUES ("{t_name}", "{weapon}", "{hp}", "{mp}", "{sp_move}", "{t_type}", "{t_user}");""")

    def find_toon(self, user):
        self.c.execute("SELECT t_name, weapons, hp, mp, sp_move, t_type FROM toons \
        WHERE t_user = \"" + user + "\";")
        creds = self.c.fetchone()
        return creds

    def kill_toon(self, user):
        self.c.execute("DELETE FROM toons WHERE t_user = \"" + user + "\";")

    def manual_query(self, sql):
        self.c.execute(sql)
