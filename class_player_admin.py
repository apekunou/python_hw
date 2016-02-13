import datetime
import db
from class_player import Player

class Player_admin(Player):

    def __init__(self, login, name = None, psw = None, session = None, money = None, ban = None, admin = 'X', id = None):

        super(Player_admin, self).__init__(login, name, psw, session, money, ban, id)
        self.admin = admin

    def load_from_db(self):
        cur = db.con.cursor()

        sql_query_login = 'SELECT `id`, `login`, `name`, `psw`, `ban`, `admin` FROM `player` WHERE login = (%(login)s);'

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
            self.admin = data[5]
        else:
            print('No data loaded from db')


    def save_to_db(self):

        cur = db.con.cursor()

        curr_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sql_player_data = {
        "login": self.login,
        "name": self.name,
        "psw": self.psw,
        "ban": self.ban,
        "admin": self.admin,
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
            sql_insert_player = 'UPDATE `player` SET `name` = %(name)s, `psw` = %(psw)s, `ban` = %(ban)s, `admin` = %(admin)s, `updated` = %(updated)s' \
                                ' WHERE `id` = %(id)s ;'
        else:
            sql_insert_player = 'INSERT INTO `player` (`login`, `name`, `psw`, `ban`, `admin`, `created`, `updated`)' \
                          ' VALUES (%(login)s, %(name)s, %(psw)s, %(ban)s, %(admin)s, %(created)s, %(updated)s);'

        cur.execute(sql_insert_player, sql_player_data)
        db.con.commit()

    def ban_player(self, player):
        player.ban = 'X'
