import json
import os
#import db
import datetime
import random

class Game(object):
    def __init__(self, sessions = []):
        self.sessions = sessions

    def start_game(self, session):
        self.sessions.append(session)

    def play_game(self):
        print('playing game')
        for session in self.sessions:
            print("playing game for session {}".format(session.id))
            res = random.randint(0,9)
            if res > 3:
                session.user.currencies['USD'] += 100
                print('User {} win! User amount is {}'.format(session.user.name,session.user.currencies['USD']))
            else:
                session.user.currencies['USD'] -= 100
                print('User {} loose! User amount is {}'.format(session.user.name,session.user.currencies['USD']))
            ach_w = 'lucky_mfk'
            ach_l = 'looser'
            if session.user.currencies['USD'] > 400 and not (ach_w in session.user.achivments):
                session.user.achivments.append(ach_w)
                print('User {} got achivment Lucky MFK'.format(session.user.name))
            if session.user.currencies['USD'] < 400 and ach_w in session.user.achivments:
                session.user.achivments.remove(ach_w)
                print('User {} lost achivment Lucky MFK'.format(session.user.name))
            if session.user.currencies['USD'] < 0 and not (ach_l in session.user.achivments):
                session.user.achivments.append(ach_l)
                print('User {} got achivment Looooser! '.format(session.user.name))
            if session.user.currencies['USD'] >= 0 and ach_l in session.user.achivments:
                session.user.achivments.remove(ach_l)
                print('User {} lost achivment Looooser! '.format(session.user.name))

        if not self.sessions:
            print('no users logged on')

    def user_logoff(self, login):
        for session in self.sessions:
            if session.user.login == login:
                session.logoff()
class Session(object):
    def __init__(self, user, game, id = None, closed = False, user_login = None, session_data = None, start_time = None, end_time = None):
        self.user = user
        self.game = game
        self.closed = closed
        self.user_login = user.login
        self.session_data = {}
        str_time = str(datetime.datetime.now())
        self.start_time = str_time[:19]
        self.end_time = end_time
        sessions_id_file_name = 'sessions_id.txt'
        id = 1
        if os.path.isfile(sessions_id_file_name):
            sessions_id_file = open(sessions_id_file_name)
            line = sessions_id_file.read()
            id = int(line)
            id += 1
        str_id = str(id)
        sessions_id_file = open(sessions_id_file_name,'w')
        sessions_id_file.write(str_id)
        sessions_id_file.close()
        self.id = id
        self.game.start_game(self)

    def as_dict_session_data(self):

         d = {
            "start_time": self.start_time,
            "end_time": self.end_time,
            "user_login": self.user_login
         }
         return d

    def save(self):
        file_name = 'sessions_data.txt'
        session_data = {}
        new_session_data = {}
        if os.path.isfile(file_name):
            file_object_read = open(file_name)
            s_file_data = file_object_read.read()
            if s_file_data:
                try:
                    session_data = json.loads(s_file_data)
                except:
                    print('error during saving session data')
                    return
        file_object = open(file_name, 'w')
        str_time = str(datetime.datetime.now())
        self.end_time =  str_time[:19]
        new_session_data = self.as_dict_session_data()
        session_data[self.id] = new_session_data
        try:
            json.dump(session_data, file_object)
        except:
            raise ValueError('error during saving session data')
            return

    def logoff(self):
        self.save()
        self.user.logoff()


class User(object):
    def __init__(self, login = None, psw = None, name = None, counters = None, achivments = [], currencies = {}, logined = False):
        self.login = login
        self.psw = psw
        self.name = name
        self.counters = counters
        self.achivments = achivments
        self.currencies = currencies
        self.logined = logined

    def as_dict_user_data(self):
         d = {
            "login": self.login,
            "name": self.name,
            "counter": self.counters,
            "achivments": self.achivments,
            "currencies": self.currencies,
         }
         return d

    def load_user_data(self):
        file_name = self.login + '_data.txt'
        file_object = open(file_name)
        s_file_data = file_object.read()
        if s_file_data:
            try:
                user_data = json.loads(s_file_data)
            except:
                print('user data file corrupted')
                return
        self.name =  user_data['name']
        self.counters =  user_data['counter']
        self.achivments =  user_data['achivments']
        self.currencies =  user_data['currencies']

    def make_login(self):
        login_data = {}
        file_name = 'login_data_all.txt'
        if not os.path.isfile(file_name):
            print('login data not found')
            return
        file_object_read = open(file_name)
        s_file_data = file_object_read.read()
        #print(s_file_data)
        if s_file_data:
            try:
                login_data = json.loads(s_file_data)
            except:
                print('login data file corrupted')
                return
        if self.login in login_data:
            if login_data[self.login] == self.psw:
                self.logined = True
                print('User {} loginned'.format(self.login))
                self.load_user_data()

    def registrate(self, login, name, psw, counters = None, achivments = None, currencies = None):
        self.login = login
        self.name = name
        self.psw = psw
        self.currencies["USD"] = 100
        print('user {} trying to registrated'.format(self.name))
        try:
            self.save_login_data()
            self.save_user_data()
            print('user {} registered'.format(self.name))
        except ValueError as err:
            print(err)

    def save_user_data(self):
        file_name = self.login + '_data.txt'
        file_object = open(file_name, 'w')
        try:
            json.dump(self.as_dict_user_data(), file_object)
        except:
            raise ValueError('error during saving user data')
            return

    def save_user_data_to_db(self):
        sql_data = {
            "login": self.login,
            "name": self.name,
        }
        print('updating user db')
       # sql_query = "INSERT INTO `users_data` (`user_login`, `user_name`, `created`, `updated`) VALUES (%(login)s, %(name)s, now(), now());"
       # cur = db.connection.cursor()
       # cur.execute(sql_query, sql_data)


    def save_login_data(self):
        login_data = {}
        file_name = 'login_data_all.txt'
        if os.path.isfile(file_name):
            file_object_read = open(file_name)
            s_file_data = file_object_read.read()
            if s_file_data:
                try:
                    login_data = json.loads(s_file_data)
                except:
                    print('login data file corrupted')
                    return
            if self.login in login_data:
                raise ValueError('user already exist')
                return
        file_object_write = open(file_name, "w")
        login_data[self.login] = self.psw
        try:
            json.dump(login_data, file_object_write)
            print('User {} login data saved'.format(self.name))
        except:
            print('error during saving user login data')

    def logoff(self):
        self.save_user_data()


if __name__ == "__main__":

    lo_game = Game()
    user1 = User()
    user1.registrate('user1_login', 'user1_name', 'user1_psw')
    user2 = User()
    user2.registrate('user2_login', 'user2_name', 'user2_psw')
    user1.make_login()
    user2.make_login()

    game = Game()
    if user1.logined:
        session = Session(user1, game)
    if user2.logined:
        session = Session(user2, game)

    for i in range(1,5):
        print('Play roud {}'.format(i))
        game.play_game()

    if user1.logined:
        game.user_logoff('user1_login')
    if user2.logined:
        game.user_logoff('user2_login')

    #session.save()

"""
    sql_data = {
    "id": 0,
    "code": "USD",
    "amount": 100,
    }

with db.connection:
    cur = db.connection.cursor()
    print('updating db')
    cur.execute(sql_query, sql_data)
"""

#    user1.counters = 1
#    user1.save_user_data()
    #user1 = User()
    #user1.registrate('user2_login', 'user2_name', 'user2_psw')


    # Emulating main loop
#    while True:
#        if i == 0:
#            print('Server startes')
#        lo_game.play_game()
        #User has connected - starting new session
#        session_init = Session(i, lo_game)
#        sessions.append(session_init)
#        for session in sessions:
#            if session.closed == True:
#                session.save()
#                sessions.remove(session)
#        if i == 5:
#            print("Server closed")
#            break
#        i += 1



