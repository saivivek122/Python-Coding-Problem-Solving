import datetime

ptime = datetime.datetime.now()
ptime = ptime.strftime("%H:%M:%S")
tday = datetime.date.today()
datetime_object = datetime.datetime.strptime(str(tday.month), "%m")
year = tday.year
full_month_name = datetime_object.strftime("%B")
print(full_month_name,"-Month Name")
print(year,"-present year")
print(tday,"-predent date")
print(ptime,"-present_time")
folder = str(tday)+'/'+str(ptime)+'_report.xml'

