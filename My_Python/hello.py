import datetime
import calendar
end = "8/05/2021"
start = "3/05/2021"
def weekday_count(start, end):
    start_date = datetime.datetime.strptime(start, '%d/%m/%Y')
    end_date = datetime.datetime.strptime(end, '%d/%m/%Y')
    week = {}
    for i in range((end_date - start_date).days):
        day = calendar.day_name[(start_date + datetime.timedelta(days=i + 1)).weekday()]
        week[day] = week[day] + 1 if day in week else 1
    if 'Saturday' in week and 'Sunday' in week:
        return week['Saturday'] + week['Sunday']
    elif 'Saturday' in week:
        return week['Saturday'] + 1
    elif 'Sunday' in week:
        return  week['Sunday']
    else:
        return 0
    #return week

week_ends = weekday_count(start,end )
print(week_ends)
tdelta = datetime.timedelta(days = week_ends )
end = datetime.datetime.strptime(end, '%d/%m/%Y')
end = (tdelta+end).date()
print(end)

