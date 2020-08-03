from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, one=None):
    if one is None:
        one = datetime.today()
        
    day_num = one.weekday()
    print(day_num)
    day_num_target = weekdays.index(dayname)
    #print(day_num_target)
    days_ago = (7 + day_num - day_num_target) % 7 
    if days_ago == 0:
        days_ago = 7
    target_date = one - timedelta(days=days_ago)
    return target_date

#print(datetime.today())
print(get_previous_byday('Saturday'))
