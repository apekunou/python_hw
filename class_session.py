import datetime
import db
class Session(object):
    def __init__(self, player_login, time_start = None, time_end = None ):
        self.player_login = player_login
        str_time = str(datetime.datetime.now())
        self.time_start = str_time[:19]
        self.time_end = time_end

    def get_end_time(self):
        str_time = str(datetime.datetime.now())
        self.time_end = str_time[:19]

    def load_from_db(self):
        pass

    def save_to_db(self):
        pass