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
        pass

    def load_from_db(self):
        sql_query_stat = 'SELECT event_type, event_data FROM log_game_events WHERE created BETWEEN (%s) AND (%s) AND event_type IN (%s,%s,%s,%s)'

        cur = db.con.cursor()
        #cur.execute(sql_query_stat, (datetime_input_start, datetime_input_end, lv_wsg_event_id, lv_wpg_event_id, lv_psg_event_id, lv_ppg_event_id))

    def save_to_db(self):

        curr_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sql_player_data = {
        "login": self.login,
        "name": self.name,
        "psw": self.psw,
        "ban": self.ban,
        "created": curr_datetime,
        "updated": curr_datetime
        }

        sql_insert_player = 'INSERT INTO `player` (`login`, `name`, `psw`, `ban`, `created`, `updated`)' \
                          ' VALUES (%(login)s, %(name)s, %(psw)s, %(ban)s, %(created)s, %(updated)s);'
        cur = db.con.cursor()
        cur.execute(sql_insert_player, sql_player_data)
        db.con.commit()