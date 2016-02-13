import json
import datetime
import db
from class_session import Session
from class_money import Money
class Player(object):
    def __init__(self, login, name = None, psw = None, session = None, money = None, ban = None, id = None ):
        self.login = login
        self.name = name
        self.id = id
        self.psw = psw
        self.session = session
        self.money = money
        self.ban = ban

    def get_id(self):
        cur = db.con.cursor()

        sql_query_login = 'SELECT `id` FROM `player` WHERE login = (%(login)s);'

        sql_login_data = {
        "login": self.login,
        }

        cur.execute(sql_query_login, sql_login_data)
        data = cur.fetchone()

        if data:
            self.id = int(data[0])
        else:
            print('No player id data loaded from db')

    def load_from_db(self):
        cur = db.con.cursor()

        sql_query_login = 'SELECT `id`, `login`, `name`, `psw`, `ban` FROM `player` WHERE login = (%(login)s);'

        sql_login_data = {
        "login": self.login,
        }

        cur.execute(sql_query_login, sql_login_data)
        data = cur.fetchone()

        if data:
            self.id = int(data[0])
            self.name = data[2]
            self.psw = data[3]
            self.ban = data[4]
        else:
            print('No player data loaded from db')


    def save_to_db(self):

        cur = db.con.cursor()

        curr_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sql_player_data = {
        "login": self.login,
        "name": self.name,
        "psw": self.psw,
        "ban": self.ban,
        "created": curr_datetime,
        "updated": curr_datetime
        }

        sql_query_login = 'SELECT `id`, `login`, `created` FROM `player` WHERE login = (%(login)s);'

        sql_login_data = {
        "login": self.login,
        }

        cur.execute(sql_query_login, sql_login_data)
        data = cur.fetchone()

        if data:
            sql_player_data["created"] = data[1]
            sql_player_data["id"] = int(data[0])
            sql_insert_player = 'UPDATE `player` SET `name` = %(name)s, `psw` = %(psw)s, `ban` = %(ban)s, `updated` = %(updated)s' \
                                ' WHERE `id` = %(id)s ;'
        else:
            sql_insert_player = 'INSERT INTO `player` (`login`, `name`, `psw`, `ban`, `created`, `updated`)' \
                          ' VALUES (%(login)s, %(name)s, %(psw)s, %(ban)s, %(created)s, %(updated)s);'

        cur.execute(sql_insert_player, sql_player_data)
        db.con.commit()