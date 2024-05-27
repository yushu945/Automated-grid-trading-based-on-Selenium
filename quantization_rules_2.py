# 先： 在这个位置添加量化交易规则并将实现量化的数据存入数据表中
# 后： 还需要实现自动完成实际的交易 PS：完成
# 之后的任务: 完善量化交易规则, 明天测试情况

# 完成建立查询持有股票数量和当完成交易时的可用数量的所有数量的修改

# 添加查询持有数量，并将数量拆分为5次
'''
5月到9月为低波动期，关闭连续买入卖出限制次数操作，波动大的时候开启
'''


# 导入自编写的函数
from data_crud import insert_trade, get_pricenumber_data, reve_price_number
from automation import GuoYuan_Buy_stock, GuoYuan_Sell_stock, GuoSheng_Buy_stock, GuoSheng_Sell_stock


# 建立全局变量用来记录买入卖出数量限制
Buy_number = 0  # 记录买入次数 每天第一次开始为0
Sell_number = 0  # 记录卖出次数  第一次开始为0
# 记录程序开始时的可用股票数量  需要每天修改  ps:记录可以卖出的次数 例子：3000股 == 3000/500=6次
Available_quantity = 7
# 记录程序开始时可以使用的资金数量  需要每天修改  ps:记录可以买入的次数 例子：可以买3000股 == 3000/500=6次
Available_Funds = 1
Allow_Buy = True  # 判断可以进行买入的条件
Allow_Sell = True  # 判断可以进行卖出的条件

# 建立量化比较函数并实现存入数据表和完成实际的交易操作
def quantitfy(old_price,old_rise,old_pcage,new_price,new_rise,new_pcage):
    # 获取全局数据
    global Buy_number
    global Sell_number
    global Available_quantity
    global Available_Funds
    global Allow_Buy
    global Allow_Sell
    print('连续买入: '+str(Buy_number)+' *** ', '连续卖出: '+str(Sell_number))  # 输出连续买入or卖出次数
    # 将获取的数据都进行float化
    old_price_float = float(old_price)
    old_rise_float = float(old_rise)
    old_pcage_float = float(old_pcage[:-1])
    # 当获取的属性中只有'-'号时，将上一次交易时的数据赋值给新数据
    if new_price == '-':
        new_price_float = old_price_float
        new_rise_float = old_rise_float
        new_pcage_float = old_pcage_float
    else:
        new_price_float = float(new_price)  # 当前面有负号时会报错 转换不了'-'
        new_rise_float = float(new_rise)
        new_pcage_float = float(new_pcage[:-1])

    # 新的百分比减去旧的百分比求出比较值差
    compare_values = new_pcage_float - old_pcage_float
    print('差值: ' + str(compare_values))
    '''
    进行比较当old_price == 0 时，表示为本日第一次比较，
    就算达不到量化要求也会将新数值返回给主函数
    '''
    if old_price_float == 0:
        # 当差值大于0.5时, 卖出部分股票
        if compare_values > 0.35:  # 原数据： 0.5
            if Available_quantity > 0:  # 判断可以卖出次数大于0时
                # 查询可用数量和所有数量
                yes_number, all_number = get_pricenumber_data()
                # 1. 实现将交易内容存入数据库
                # 2. 实现自动化的交易
                trade_number = 400  # 设定需要交易的股票数量
                trade_state = '卖出'  # 设定发生交易的类型
                print('卖出')
                # 将交易的内容存入数据库中
                insert_trade(trade_state,trade_number,new_price_float,new_rise_float,new_pcage)
                '''自动化实现量化交易'''
                # GuoYuan_Sell_stock(trade_number)
                GuoSheng_Sell_stock(trade_number, new_price_float)  # 这里添加一个准确的价格
                # 交易成功后修改数值，并将修改的数值传入数据库中
                yes_number = yes_number - trade_number  # 卖出后的可用数量
                all_number = all_number - trade_number  # 卖出后的所有数量
                reve_price_number(yes_number, all_number)  # 修改数据中的值
                Sell_number = Sell_number + 1  # 记录卖出次数
                Available_quantity = Available_quantity - 1  # 修改可以买入的次数
                # 当卖出一次后，资金回笼 可买入次数+1
                Available_Funds = Available_Funds + 1
            else:
                pass  # 当买入次数为0时不执行
        # 当差值小于-0.5时, 买入部分股票
        elif compare_values < -0.35:  # 原数据： 0.5
            if Available_Funds > 0:  # 判断可以买入的次数是否大于0
                # 查询可用数量和所有数量
                yes_number, all_number = get_pricenumber_data()
                # 1. 实现将交易内容存入数据库
                # 2. 实现自动化的交易
                trade_number = 400  # 设定需要交易的股票数量
                trade_state = '买入'  # 设定发生交易的类型
                print('买入')
                insert_trade(trade_state,trade_number,new_price_float,new_rise_float,new_pcage)
                '''自动化实现量化交易'''
                # GuoYuan_Buy_stock(trade_number)
                GuoSheng_Buy_stock(trade_number, new_price_float)
                # 交易成功后修改数值，并将修改的数值传入数据库中
                yes_number = yes_number  # 买入后的可用数量
                all_number = all_number + trade_number  # 买入后的所有数量
                reve_price_number(yes_number, all_number)  # 修改数据中的值
                Buy_number = Buy_number + 1  # 记录买入次数
                Available_Funds = Available_Funds - 1 # 修改可以买入的次数
        return new_price, new_rise, new_pcage
    # 当不是第一次比较后进入else
    else:
        # 当差值大于0.5时, 卖出部分股票
        if compare_values > 0.35:  # 原数据： 0.5
            # 查询可用数量和所有数量
            yes_number, all_number = get_pricenumber_data()
            # 1. 实现将交易内容存入数据库
            # 2. 实现自动化的交易
            trade_number = 400  # 设定需要交易的股票数量
            trade_state = '卖出'  # 设定发生交易的类型
            if Available_quantity > 0:  # 判断可以卖出次数大于0时
                # 加入一个判断卖出次数
                if Sell_number >= 3:
                    # 加入一个判断差值
                    if compare_values > 0.5:      # 这个位置是添加一个高波动连续卖出保险，暂时不需要
                        # 实现卖出操作
                        print('卖出')
                        # 将交易的内容存入数据库中
                        insert_trade(trade_state, trade_number, new_price_float, new_rise_float, new_pcage)
                        '''自动化实现量化交易'''
                        # GuoYuan_Sell_stock(trade_number)
                        GuoSheng_Sell_stock(trade_number, new_price_float)
                        # 交易成功后修改数值，并将修改的数值传入数据库中
                        yes_number = yes_number - trade_number  # 卖出后的可用数量
                        all_number = all_number - trade_number  # 卖出后的所有数量
                        reve_price_number(yes_number, all_number)  # 修改数据中的值
                        Sell_number = Sell_number + 1  # 增加交易记录次数
                        Available_quantity = Available_quantity - 1  # 修改可以卖出的次数
                        # 当卖出一次后，资金回笼 可买入次数+1
                        Available_Funds = Available_Funds + 1
                        return new_price, new_rise, new_pcage
                    else:
                        # 当判断连续卖出次数大于等于3时并且差值没有超过0.8 时，返回老值
                        return old_price, old_rise, old_pcage
                else:
                    print('卖出')
                    # 将交易的内容存入数据库中
                    insert_trade(trade_state, trade_number, new_price_float, new_rise_float, new_pcage)
                    '''自动化实现量化交易'''
                    # GuoYuan_Sell_stock(trade_number)
                    GuoSheng_Sell_stock(trade_number, new_price_float)
                    # 交易成功后修改数值，并将修改的数值传入数据库中
                    yes_number = yes_number - trade_number  # 卖出后的可用数量
                    all_number = all_number - trade_number  # 卖出后的所有数量
                    reve_price_number(yes_number, all_number)  # 修改数据中的值
                    Sell_number = Sell_number + 1  # 增加交易记录次数
                    Buy_number = 0  # 重置连续买入的次数
                    Available_quantity = Available_quantity - 1  # 修改可以卖出的次数
                    # 当卖出一次后，资金回笼 可买入次数+1
                    Available_Funds = Available_Funds + 1
                    return new_price, new_rise, new_pcage
            else:
                # 当没有卖出次数时，返回老值
                return old_price, old_rise, old_pcage
        # 当差值小于-0.5时, 买入部分股票
        elif compare_values < -0.35:  # 原数据： 0.5
            # 查询可用数量和所有数量
            yes_number, all_number = get_pricenumber_data()
            # 1. 实现将交易内容存入数据库
            # 2. 实现自动化的交易
            trade_number = 400  # 设定需要交易的股票数量
            trade_state = '买入'  # 设定发生交易的类型
            if Available_Funds > 0:  # 判断可以买入的次数是否大于0
                # 判断买入次数
                if Buy_number >= 3:
                    # 加入一个判断compare_values
                    if compare_values < -0.5:       # 这个位置是添加一个高波动连续卖出保险，暂时不需要
                        print('买入')
                        insert_trade(trade_state, trade_number, new_price_float, new_rise_float, new_pcage)
                        '''自动化实现量化交易'''
                        # GuoYuan_Buy_stock(trade_number)
                        GuoSheng_Buy_stock(trade_number, new_price_float)
                        # 交易成功后修改数值，并将修改的数值传入数据库中
                        yes_number = yes_number  # 买入后的可用数量
                        all_number = all_number + trade_number  # 买入后的所有数量
                        reve_price_number(yes_number, all_number)  # 修改数据中的值
                        Buy_number = Buy_number + 1  # 记录
                        Available_Funds = Available_Funds - 1  # 修改可以买入的次数
                        return new_price, new_rise, new_pcage
                    else:
                        # 当判断连续卖出次数大于等于3时并且差值没有超过0.8 时，返回老值
                        return old_price, old_rise, old_pcage
                else:
                    print('买入')
                    insert_trade(trade_state, trade_number, new_price_float, new_rise_float, new_pcage)
                    '''自动化实现量化交易'''
                    # GuoYuan_Buy_stock(trade_number)
                    GuoSheng_Buy_stock(trade_number, new_price_float)
                    # 交易成功后修改数值，并将修改的数值传入数据库中
                    yes_number = yes_number  # 买入后的可用数量
                    all_number = all_number + trade_number  # 买入后的所有数量
                    reve_price_number(yes_number, all_number)  # 修改数据中的值
                    Buy_number = Buy_number + 1  # 记录交易次数
                    Sell_number = 0  # 重置卖出次数
                    Available_Funds = Available_Funds - 1  # 修改可以买入的次数
                    return new_price, new_rise, new_pcage
            else:
                # 当没有购买次数后返回老值
                return old_price, old_rise, old_pcage
        # 当差值既不大于0.5也不小于-0.5时, 返回旧的数据
        else:
            return old_price, old_rise, old_pcage





if __name__ == '__main__':
    old_price = '3.331'
    old_rise = '-0.004'
    old_pcage = '-0.15%'
    new_price = '3.500'
    new_rise = '0.500'
    new_pcage = '-0.4%'
    quantitfy(old_price,old_rise,old_pcage,new_price,new_rise,new_pcage)