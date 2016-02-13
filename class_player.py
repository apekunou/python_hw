import json
import datetime
from session import Session
from money import Money
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
        pass

    def save_to_db(self):
        pass