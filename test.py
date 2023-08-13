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

# print(datetime.now())

while 1:
    x = datetime.today()

    # time critical task to execute only when site refreshed
    if x > z:
        # click on register button using css_selector (number of modules may affect xpath)
        print(datetime.now())
        break

### while loop higher precision in keeping track of time than sleep