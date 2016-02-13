import json
import db
import datetime
class Money(object):
    def __init__(self, player_login, curr, amount = None, player_id = None):
        self.player_login = player_login
        self.curr = curr
        self.amount = amount
        self.player_id = player_id

    def as_dict_money(self):
        money_as_dict = {
            'curr': self.curr,
            'amount': self.amount,
        }
        return money_as_dict

    def save_to_file(self, file_object):
        file_name = self.player_login + 'money_data.txt'
        file_object = open(file_name, 'w')
        try:
            json.dump(self.as_dict_money(), file_object)
        except:
            raise ValueError('error during saving user money data')
            return

    def load_from_file(self, file_object):
        file_name = self.player_login + 'money_data.txt'
        file_object = open(file_name)
        s_file_data = file_object.read()
        if s_file_data:
            try:
                money_data = json.loads(s_file_data)
            except:
                print('user money data file corrupted')
                return
        self.curr =  money_data['curr']
        self.amount =  money_data['amount']

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

        sql_money_data = {
        "player_id": self.player_id,
        "curr": self.curr,
        "amount": self.amount,
        "created": curr_datetime,
        "updated": curr_datetime
        }

        sql_query_money = 'SELECT `id`, `amount`, `created` FROM `money` WHERE `player_id` = (%(player_id)s) ' \
                                                                         'AND `curr` = (%(curr)s);'


        cur.execute(sql_query_money, sql_money_data)
        data = cur.fetchone()

        if data:
            sql_money_data["id"] = int(data[0])
            sql_money_data["amount"] = data[1]
            sql_money_data["created"] = data[2]
            sql_insert_money = 'UPDATE `money` SET `amount` = %(amount)s, `updated` = %(updated)s' \
                                ' WHERE `id` = %(id)s ;'
        else:
            sql_insert_money = 'INSERT INTO `money` (`player_id`, `curr`, `amount`, `created`, `updated`)' \
                          ' VALUES (%(player_id)s, %(curr)s, %(amount)s, %(created)s, %(updated)s);'

        cur.execute(sql_insert_money, sql_money_data)
        db.con.commit()

    def load_from_db(self):
        cur = db.con.cursor()

        if not self.player_id:
            try:
                self.get_player_id()
            except:
                return

        sql_money_data = {
        "player_id": self.player_id,
        "curr": self.curr,
        }
        sql_query_money = 'SELECT `amount` FROM `money` WHERE `player_id` = (%(player_id)s) ' \
                                                         'AND `curr` = (%(curr)s);'


        cur.execute(sql_query_money, sql_money_data)
        data = cur.fetchone()

        if data:
            self.amount = data[0]
        else:
            print('No money data selected')

