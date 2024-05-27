import sqlite3
from datetime import datetime
conn = sqlite3.connect('quantify.db')
cursor = conn.cursor()

# 创建记录持有股票数量的数据库
def create_PriceNumber():
    # 仅限试用！ 正式使用的时候需要删除该字段
    sql = '''DROP TABLE IF EXISTS `price_number`'''
    cursor.execute(sql)
    # 以上正式使用时删除删除
    sql_price = '''CREATE TABLE price_number
                (
                id integer primary key ,
                yes_number int ,
                all_number int
                );'''
    cursor.execute(sql_price)
    return None

# 创建记录交易情况的数据表
def create_trade():
    # 仅限试用！ 正式使用的时候需要删除该字段
    sql = '''DROP TABLE IF EXISTS `trade_logs`'''
    cursor.execute(sql)
    # 以上正式使用时删除删除
    sql_trade = '''CREATE TABLE trade_logs
                (
                id integer primary key ,
                trade_time varchar(64) ,
                trade_state varchar(64) ,
                trade_number int , 
                trade_ptice float, 
                trade_Rise float,
                trade_pcage varchar(24)
                )'''
    cursor.execute(sql_trade)
    return None

# 创建插入交易情况表的函数
def insert_trade(trade_state, trade_number, new_price, new_rise, new_pcage):
    # 获取发生交易的时间
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    data = (formatted_datetime, trade_state, trade_number, new_price, new_rise, new_pcage)
    sql = '''INSERT INTO trade_logs (trade_time,trade_state,trade_number,trade_ptice,trade_Rise,trade_pcage)
            VALUES (?,?,?,?,?,?)'''
    cursor.execute(sql,data)
    conn.commit()
    # print('完成')
    return None

# 创建开盘价格表
def create_save_frist():
    # 仅限试用！ 正式使用的时候需要删除该字段
    sql = '''DROP TABLE IF EXISTS `save_frist`'''
    cursor.execute(sql)
    # 以上正式使用时删除删除
    sql_save = '''CREATE TABLE save_frist
                (
                id integer primary key ,
                frist_time varchar(64) ,
                frist_price float , 
                frist_rise float , 
                frist_pcage varchar(24)
                )'''
    cursor.execute(sql_save)
    return None

# 创建插入开盘价格表的函数
def insert_save_frist(price, rise, pcage):
    # 获取发生该事件的时间
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # print("日期和时间:", formatted_datetime)
    data_save = (formatted_datetime, price, rise, pcage)
    sql = '''INSERT INTO save_frist (frist_time,frist_price,frist_rise,frist_pcage) VALUES (?,?,?,?)'''
    cursor.execute(sql, data_save)
    conn.commit()
    # print('完成')
    return None


# 创建查询数据库price数据的函数
def get_pricenumber_data():
    sql = '''SELECT * FROM price_number'''
    cursor.execute(sql)
    # 获取到值
    data = cursor.fetchall()
    # print(data)
    y_number = data[0][1]  # 获取到当日可用数量
    # print(y_number)
    all_number = data[0][2]  # 获取所有数量
    return y_number, all_number


# 修改数据库price的函数
def reve_price_number(yes_number, all_number):
    # print(yes_number)
    sql_yes = '''UPDATE price_number SET yes_number=? WHERE id=1'''
    cursor.execute(sql_yes, (yes_number,))
    sql_all = '''UPDATE price_number SET all_number=? WHERE id=1'''
    cursor.execute(sql_all, (all_number,))
    conn.commit()
    return None




if __name__ == '__main__':
    reve_price_number(1000, 1500)