
from class_player import Player
from class_session import Session
from class_money import Money
from class_player_admin import Player_admin

player1 = Player('a1@b', 'name1', 'psw_2')
print(player1.login)
player1.save_to_db()

session1 = Session('a1@b')
session1.save_to_db()
print('session start time is {}'.format(session1.time_start))

player2 = Player('a2@b', 'name2', 'psw_2')
print(player1.login)
player1.save_to_db()

player3 = Player('a1@b')
player3.load_from_db()
print('player psw is {}'.format(player3.psw))

money_p1_usd = Money('a1@b', 'usd', 200)
money_p1_usd.save_to_db()

money_p2_usd = Money('a1@b', 'usd')
money_p2_usd.load_from_db()
print('money amount is {}'.format(money_p2_usd.amount))

player1.money = money_p1_usd
print('player {} money amount is {}'.format(player1.name, player1.money.amount))

admin1 = Player_admin('ad1@c', 'admin1', 'psw_admin')
print('player {} login is {}'.format(admin1.name, admin1.login))
print('player {} login is admin {}'.format(admin1.name, admin1.admin))
admin1.save_to_db()

admin2 = Player_admin('ad1@c')
admin2.load_from_db()
print('loaded from db password of player {} login is {}'.format(admin2.name, admin2.psw))

admin2.ban_player(player2)
print('player {} is banned {}'.format(player2.name, player2.ban))

session2 = Session('a1@b')
session2.load_from_db()
print('session 2 time finish is {}'.format(session2.time_finish))

