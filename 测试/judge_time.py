from datetime import datetime, time

current_datetime = datetime.now().time()
# formatted_datetime = current_datetime.strftime("%H:%M:%S")

other_time_after = time(9, 25, 0)
other_time_last = time(9, 30, 0)
if other_time_after < current_datetime <other_time_last:
    print(1)
else:
    print(2)

