import datetime

# using now() to get current time
ptime = datetime.datetime.now()
ptime = ptime.strftime("%H:%M:%S")
tday = datetime.date.today()
current_date = datetime.date.today()
month_num = current_date.month
datetime_object = datetime.datetime.strptime(month_num, "%m")

# Printing value of now.
print("Time now at greenwich meridian is : "
      , end="")
print(ptime)
print(tday)
folder = str(tday)+'/'+str(ptime)+'_report.xml'
print(folder)