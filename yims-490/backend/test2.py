from datetime import datetime

current_time = str(datetime.now().time()).split('.')[0]
current_date = datetime.now().date()
date = datetime.now().strftime("%Y-%m-%d")
print(current_time, current_date, type(date))