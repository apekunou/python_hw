import datetime
import db
class Session(object):
    def __init__(self, player_login, time_start = None, time_finish = None, player_id = None ):
        self.player_login = player_login
        self.player_id = player_id
        if time_start:
            self.time_start = time_start
        else:
            self.time_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_finish = time_finish

    def get_player_id(self):
        cur = db.con.cursor()

        sql_query_login = 'SELECT `id` FROM `player` WHERE login = (%(login)s);'

        sql_login_data = {
        "login": self.player_login,
        }

        cur.execute(sql_query_login, sql_login_data)
        data = cur.fetchone()

        if data:
            self.player_id = int(data[0])
        else:
            print('No player id data loaded from db')
            raise ValueError('No player id data loaded from db')

    def save_to_db(self):

        cur = db.con.cursor()

        if not self.player_id:
            try:
                self.get_player_id()
            except:
                return

        curr_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sql_session_data = {
        "player_id": self.player_id,
        "time_start": self.time_start,
        "time_finish": curr_datetime
        }

        sql_query_session = 'SELECT `id`, `time_finish` FROM `sessions` WHERE `player_id` = (%(player_id)s) ' \
                                                                         'AND `time_start` = (%(time_start)s);'


        cur.execute(sql_query_session, sql_session_data)
        data = cur.fetchone()

        if data:
            sql_session_data["id"] = int(data[0])
            sql_session_data["time_finish"] = data[1]
            sql_insert_session = 'UPDATE `sessions` SET `time_finish` = %(time_finish)s' \
                                ' WHERE `id` = %(id)s ;'
        else:
            sql_insert_session = 'INSERT INTO `sessions` (`player_id`, `time_start`, `time_finish`)' \
                          ' VALUES (%(player_id)s, %(time_start)s, %(time_finish)s);'

        cur.execute(sql_insert_session, sql_session_data)
        db.con.commit()

    def load_from_db(self):
        cur = db.con.cursor()

        if not self.player_id:
            try:
                self.get_player_id()
            except:
                return

        sql_session_data = {
        "player_id": self.player_id,
        "time_start": self.time_start,
        }

        sql_query_session = 'SELECT `time_finish` FROM `sessions` WHERE `player_id` = (%(player_id)s) ' \
                                                                   'AND `time_start` = (%(time_start)s);'


        cur.execute(sql_query_session, sql_session_data)
        data = cur.fetchone()

        if data:
            self.time_finish = data[0]
        else:
            print('No session data selected')