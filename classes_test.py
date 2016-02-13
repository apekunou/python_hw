
from class_player import Player
from class_session import Session
from class_money import Money
from class_player_admin import Player_admin
#def __init__(self, login, name = None, psw = None, session = None, money = None, ban = None, id = None ):
player1 = Player('a4@b', 'name1', 'psw_changed3')
print(player1.login)
player1.save_to_db()

player2 = Player('a3@b')
player2.load_from_db()
print(player2.psw)

money_p1_usd = Money('a3@b', 'usd', 200)
money_p1_usd.save_to_db()

money_p2_usd = Money('a4@b', 'usd')
print(money_p2_usd.amount)



'''
admin = Player_admin('a1@c', 'name1', 'psw1')
print(admin.login)
print(admin.admin)
admin.save_to_db()
'''