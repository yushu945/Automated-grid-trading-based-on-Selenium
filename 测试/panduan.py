import time


allow_buy = True

while True:
    time.sleep(2)
    if allow_buy:
        print(1)
        allow_buy = False
    else:
        print(2)
        allow_buy = True