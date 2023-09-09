import time
from datetime import datetime

x = datetime.today()
year = x.year
month = x.month
day = x.day

z = datetime(year, month, day, 0, 25, 59 ,9000)

x = datetime.now()
# print('Sleeping for ', (z-x).seconds + (z-x).microseconds/100000 , 'seconds')

# time.sleep((z-x).seconds + (z-x).microseconds/100000)

### while loop higher precision in keeping track of time than sleep


def check_sleep(amount):
    start = datetime.now()
    time.sleep(amount)
    end = datetime.now()
    delta = end-start
    return delta.seconds + delta.microseconds/1000000.

error = sum(abs(check_sleep(0.050)-0.050) for i in range(100))*10
print ("Average error is %0.2fms" % error)


### Average error is 0.29ms for 0.05ms m which could be significant if multiplied 
