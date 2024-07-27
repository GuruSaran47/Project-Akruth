import time as time_now
#params_of_time = ["tm_year","tm_mon","tm_mday","tm_hour","tm_min","tm_sec","tm_wday","tm_yday","tm_isdst"]



def getDate():
    time = time_now.gmtime()
    day = time.tm_mday
    month = time.tm_mon
    year = time.tm_year
    date = str(day)+"-"+str(month)+"-"+str(year)
    return date

def getTime():
    time = time_now.gmtime()
    hour = time.tm_hour 
    min = time.tm_min
    sec = time.tm_sec
    current_time = str(hour)+":"+str(min)+":"+str(sec)
    return current_time
