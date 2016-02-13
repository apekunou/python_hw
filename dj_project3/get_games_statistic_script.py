import sys
import datetime
import MySQLdb
import ast

lv_psg_event_id = 3
lv_wsg_event_id = 4
lv_ppg_event_id = 6
lv_wpg_event_id = 7

con = MySQLdb.connect('localhost', 'root', 'root', 'xo_db')

date = sys.argv[1]
str_dates = date.split('-')
year = int(str_dates[0])
mm = int(str_dates[1])
dd = int(str_dates[2])
date_input = datetime.datetime(year, mm, dd)
datetime_input_start = datetime.datetime(year, mm, dd, 00, 00, 00)
datetime_input_end = datetime.datetime(year, mm, dd, 23, 59, 59)
cur_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sql_create_table = "CREATE TABLE IF NOT EXISTS stat_player_games(" \
                   "id INT AUTO_INCREMENT," \
                   "target_date DATE," \
                   "game_count INT," \
                   "xp_amount INT," \
                   "created DATETIME," \
                   "PRIMARY KEY (id) );"


cur = con.cursor()
cur.execute(sql_create_table)
con.commit()

sql_query_stat = 'SELECT event_type, event_data FROM log_game_events WHERE created BETWEEN (%s) AND (%s) AND event_type IN (%s,%s,%s,%s)'

cur = con.cursor()
cur.execute(sql_query_stat, (datetime_input_start, datetime_input_end, lv_wsg_event_id, lv_wpg_event_id, lv_psg_event_id, lv_ppg_event_id))

data_dict = {}
xp_amount = 0
game_count = 0
for data in cur.fetchall():
    event_type = data[0]
    event_data = data[1]
    if event_type == lv_psg_event_id or event_type == lv_ppg_event_id:
        game_count += 1
    try:
        data_dict = ast.literal_eval(event_data)
        xp_amount += data_dict['exp']
    except:
        pass

sql_stat_data = {
    "target_date": date_input,
    "game_count": game_count,
    "xp_amount": xp_amount,
    "created": cur_datetime,
}

sql_insert_stat = 'INSERT INTO `stat_player_games` (`target_date`, `game_count`, `xp_amount`, `created`) VALUES (%(target_date)s, %(game_count)s, %(xp_amount)s, %(created)s);'
cur = con.cursor()
cur.execute(sql_insert_stat, sql_stat_data)
con.commit()


