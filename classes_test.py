
from class_player import Player
from class_session import Session
from class_money import Money
from class_player_admin import Player_admin
#def __init__(self, login, name = None, psw = None, session = None, money = None, ban = None, id = None ):
player1 = Player('a1@b', 'name1', 'psw1')
print(player1.login)
player1.save_to_db()

admin = Player_admin('a1@c', 'name1', 'psw1')
print(admin.login)
print(admin.admin)
admin.save_to_db()
