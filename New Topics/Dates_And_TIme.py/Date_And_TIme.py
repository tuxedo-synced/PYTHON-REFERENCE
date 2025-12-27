import datetime

date = datetime.date(2025,1,13)
print(date)
today = datetime.date.today()
print(today)
time = datetime.time(12,30,45)
print(time)
now = datetime.datetime.now()
print(now)
now = now.strftime("%m-%d-%Y %H:%M:%S")
print(now)
target_datetime = datetime.datetime(year=2000,month=1,day=2,hour=12,minute=45,second=35)
print(target_datetime)
current_datetime = datetime.datetime.now()
if target_datetime < current_datetime:
    print("Target day has passed")
else:
    print("Target date has not passed")
