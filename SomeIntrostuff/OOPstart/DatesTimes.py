import datetime

date = datetime.date(2025,1,13)
today= datetime.date.today()
time = datetime.time(12,30,9)

#returns date and time
now=datetime.datetime.now()
#format to own style
now = now.strftime("%H:%M:%S %m-%d-%Y")

target= datetime.datetime(2030,5,30,12,30,1)
current=datetime.datetime.now()

if target<current:
    print("Target date has already passed")
else:
    print("Target date has not passed")


print(date)
print(today)
print(time)
print(now)