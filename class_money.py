import json
import db
class Money(object):
    def __init__(self, player_login, curr, amount):
        self.player_login = player_login
        self.curr = curr
        self.amount = amount

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

    def save_to_db(self):
        pass

    def load_from_db(self):
        pass

