from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import _thread as thread


x = datetime.today()
year = x.year
month = x.month
day = x.day

URL = "https://venus2.wis.ntu.edu.sg/ADFSSSO2/User/Login.aspx?app=https://wis.ntu.edu.sg/pls/webexe88/srce_smain_s.Notice_O"

### Step 1 : Download ChromeDriver and copy path to chromedriver.exe here ###
chrome_driver_path = "C:\PythonDev\Selenium\chromedriver.exe"

### Step 2 : Enter Username here ###
user_name = "c210075"

### Step 3 : Enter Password here ###
password = "Jy@2015097"

### Click Path ###
badminton_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/ul/li[4]/table[2]/tbody/tr[1]/td/input'
slot_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[84]/td[9]/input'

gym_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/ul/li[4]/table[2]/tbody/tr[6]/td/input'
gym_slot_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[262]/td[2]/input'

confirmation_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/input[18]'



def main(hr, min, sec, mili):
    z = datetime(year, month, day, hr, min, sec, mili)

    # initialise webdriver 
    driver = webdriver.Chrome()
    driver.get(URL)

    # pass the basic authentication using src url 
    login_URL = "https://" + user_name + ":" + password + "@" + driver.current_url[8:]
    driver.get(login_URL)

    while 1:
        x = datetime.today()

        # time critical task to execute only when site refreshed
        if x > z:
            # accsessing the sport specific booking list
            button1 = driver.find_element(By.XPATH, gym_path)
            button1.click()
            break

    time.sleep(1.5)
    # selecting the slot
    button2 = driver.find_element(By.XPATH, gym_slot_path)
    button2.click()

    time.sleep(0.5)
    # confirming slot
    button3 = driver.find_element(By.XPATH, confirmation_path)
    button3.click()
    print("slot booked succesfully")

try:
    # Step 4(final) : Set time of booking, usually 23:59
    # thread.start_new_thread(main, (23,59,50,0000))
    # thread.start_new_thread(main, (23,59,51,0000))
    # thread.start_new_thread(main, (23,59,52,0000))
    # thread.start_new_thread(main, (23,59,53,0000))
    # thread.start_new_thread(main, (23,59,54,0000))
    # thread.start_new_thread(main, (23,59,55,0000))

    ### start time open for tuning as login expected to delay
    thread.start_new_thread(main, (x.hour, x.minute, x.second, x.microsecond))

except:
    print("Error: unable to start thread")

while 1:
    pass