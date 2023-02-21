from datetime import datetime, timedelta
today = datetime.now().replace(microsecond=0)
day = timedelta(1)
time = today - day
dif = today - time
print(dif.total_seconds())

