# Working with Dates and Times

from datetime import datetime, date, timezone, timedelta
import time

print(datetime(1995, 10, 18, 23, 11, 59))  # year, month, date, hour, minute, second
print(date(1995, 10, 18))  # year, month, date
print(date.today())  # Date of today
print(datetime.now())  # Current date time (including hour, minute, second)
diff = datetime.now() - datetime(1995, 10, 18, 22, 10, 13)
print(diff)
print(diff.days)
print(diff.seconds)
print(diff.microseconds)
next10days = datetime.now() + timedelta(days = 10, seconds = 100, microseconds = 1000)
print(next10days)
print(time.ctime(123148249823))  # Convert epoch time (seconds) to datetime
print(time.time())  # Epoch time in seconds
print(time.localtime())  # tutple of time
print(time.localtime(99999999))  # tuple of time based on epoch time
print(time.strftime("%Y m %m %d %H.%M.%S", time.localtime()))  # Format a time
time_str = "Sat Mar 11 08:20:10 +0000 2017"
time_fmt = "%a %b %d %H:%M:%S +0000 %Y"
time_tup = time.strptime(time_str, time_fmt)
print(time_tup)  # Convert time string to tuples
print(datetime.fromtimestamp(time.mktime(time_tup)))  # tuple => epoch => datetime
time.sleep(5)  # Current thread sleeps for 5 seconds

