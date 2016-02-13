import datetime
import db
from class_player import Player

class Player_admin(Player):

    def __init__(self, login, name = None, psw = None, session = None, money = None, ban = None, admin = 'X', id = None):

        super(Player_admin, self).__init__(login, name, psw, session, money, ban, id)
        self.admin = admin

    def save_to_db(self):

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

        sql_insert_player = 'INSERT INTO `player` (`login`, `name`, `psw`, `ban`, `admin`, `created`, `updated`)' \
                          ' VALUES (%(login)s, %(name)s, %(psw)s, %(ban)s, %(admin)s, %(created)s, %(updated)s);'
        cur = db.con.cursor()
        cur.execute(sql_insert_player, sql_player_data)
        db.con.commit()

    def ban_player(self, player_login):
        pass
