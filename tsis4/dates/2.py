from datetime import datetime, timedelta
today = datetime.now()
day = timedelta(1)
print((today - day).strftime("%y-%m-%d"))
print(today.strftime("%y-%m-%d"))
print((today + day).strftime("%y-%m-%d"))