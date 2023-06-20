from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import _thread as thread

x = datetime.today()
year = x.year
month = x.month
day = x.day


### Step 1 : Install selenium using the following command ###
### pip install selenium ###


### Step 2 : Enter Username here ###
user_name = ""


### Step 3 : Enter Password here ###
password = ""


### Step 4 : Specify exact paths for the booking (retrieve using XPATH) ###
URL = "https://wish.wis.ntu.edu.sg/pls/webexe/ldap_login.login?w_url=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_planner.main"

uid_submit_path = '//*[@id="top"]/div/section[2]/div/div/center[1]/form/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input[1]'

pw_submit_path = '//*[@id="top"]/div/section[2]/div/div/form/center[1]/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]'

register_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr[1]/td[2]/table/tbody/tr[12]/td/form/input[1]'


def main(hr, min, sec, mili):
    z = datetime(year, month, day, hr, min, sec, mili)

    # initialise webdriver 
    driver = webdriver.Chrome()
    driver.get(URL)

    # enter user name
    user_name_field = driver.find_element(By.ID, 'UID')
    user_name_field.send_keys(user_name)

    button1 = driver.find_element(By.XPATH, uid_submit_path)
    button1.click()

    # enter password
    pw_field = driver.find_element(By.ID, 'PW')
    pw_field.send_keys(password)

    button2 = driver.find_element(By.XPATH, pw_submit_path)
    button2.click()
    time.sleep(1)

    while 1:
        x = datetime.today()

        # time critical task to execute only when site refreshed
        if x > z:
            # accsessing the sport specific booking list
            button3 = driver.find_element(By.XPATH, register_path)
            button3.click()
            break




try:
    # Step 5(final) : Set time of booking, usually 23:59

    # thread.start_new_thread(main, (23,59,50,0000))
    # thread.start_new_thread(main, (23,59,51,0000))
    # thread.start_new_thread(main, (23,59,52,0000))
    # thread.start_new_thread(main, (23,59,53,0000))
    # thread.start_new_thread(main, (23,59,54,0000))
    thread.start_new_thread(main, (x.hour, x.minute, x.second, x.microsecond))

    ### start time open for tuning as login expected to delay

except:
    print("Error: unable to start thread")

while 1:
    pass