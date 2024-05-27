input_string = '-9.60-9.06%'

# 找到第二个 '-' 号的位置
x = input_string.find('-',1)
print(x)
second_dash_index = input_string.find('-', input_string.find('-') + 1)
print(second_dash_index)

# 如果找到第二个 '-' 号，则进行拆分
if second_dash_index != -1:
    part1 = input_string[:second_dash_index]
    part2 = input_string[second_dash_index:]

    print("第一部分:", part1)
    print("第二部分:", part2)
else:
    print("未找到第二个'-'号")