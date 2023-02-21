from datetime import datetime, timedelta
today = datetime.now()
day = today - timedelta(days=5)
x = day
print(x.strftime("%y-%m-%d"))