from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re
import _thread as thread
import time

# to keep browser opening after execution
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

x = datetime.today()
year = x.year
month = x.month
day = x.day


### Step 1 : Install selenium using the following command ###
# pip install selenium (deprecated) 

### Step 2 : Enter Username here (with @student) ###
user_name = ""


### Step 3 : Enter Password here ###
password = ""


### Step 4 : Specify exact paths for the booking (retrieve using XPATH), UNCOMMENT the sports desired ###
### The slot path can be modify tr -> row, td -> col ###
### Badminton ###
booking_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/ul/li[4]/table[2]/tbody/tr[1]/td/input'
slot_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[19]/td[9]/input'

### Gym ###
# booking_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/ul/li[4]/table[2]/tbody/tr[6]/td/input'
# slot_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[10]/td[2]/input'


### Constants ###
URL = "https://venus2.wis.ntu.edu.sg/ADFSSSO2/User/Login.aspx?app=https://wis.ntu.edu.sg/pls/webexe88/srce_smain_s.Notice_O"
confirmation_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/input[18]'
page_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form'


### Main Function ###
def main(hr, min, sec, mili):
    z = datetime(year, month, day, hr, min, sec, mili)

    # initialise webdriver 
    ## fixed 26/8/2023, chromedriver version 116
    service = Service(executable_path = 'C:/Users/teoji/Selenium/chromedriver/chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service = service, options = options)
    driver.get(URL)

    # pass the basic authentication using src url (deprecated)
    # login_URL = "https://" + user_name + ":" + password + "@" + driver.current_url[8:]
    # driver.get(login_URL)

    # new login method (updated 29/07/2023)
    # enter user name
    user_name_field = driver.find_element(By.ID, 'userNameInput')
    user_name_field.send_keys(user_name)

    # Enter password
    password_field = driver.find_element(By.ID, 'passwordInput')
    password_field.send_keys(password)

    # Login
    login_button = driver.find_element(By.ID, 'submitButton')
    login_button.click()

    # Click link when time is up 
    # while 1:
    #     x = datetime.today()

    #     # time critical task to execute only when site refreshed
    #     if x > z:
    #         # accsessing the sport specific booking list
    #         button1 = driver.find_element(By.XPATH, booking_path)
    #         button1.click()
    #         break
    
    ### Determine whether page is loaded

    # set a timeout value
    wait_page = WebDriverWait(driver, 10)
    # set attempt limit for alternative slots 
    attempt = 0 
    max_attempts = 10
    # find index value using regular expression (RE)
    match = re.search(r'/tr\[(\d+)\]', slot_path)
    if match: 
        index = int(match.group(1))
    else: 
        print('Index not found in Slot Path')
        exit()
    attempt_path = slot_path

    try:
        while 1:
            x = datetime.today()

            if x >= z:
                print('time is up')
                button1 = driver.find_element(By.XPATH, booking_path)
                button1.click()
                break
            else:
                print('Time is not up, Sleeping for ', (z-x).seconds, ' seconds')
                print((z-x).seconds + (z-x).microseconds/100000)
                time.sleep((z-x).seconds + (z-x).microseconds/100000)


        # wait for document.readyState to be 'complete'
        wait_page.until(EC.presence_of_element_located((By.XPATH, page_path)))

        while attempt < max_attempts:
            try: 
                # throw exception if slot not available
                button2 = driver.find_element(By.XPATH, attempt_path)
                # if slot is available
                print('Slot is Available!')
                button2.click()

                # wait until slot confirmation page is loaded
                wait_page.until(EC.presence_of_element_located((By.XPATH, confirmation_path)))
                print('Confirmation page is fully loaded')

                # confirming slot
                button3 = driver.find_element(By.XPATH, confirmation_path)
                button3.click()
                print('Slot booked succesfully!')
                break

            except NoSuchElementException:
                print('Slot is not available')
                # try other slot 
                attempt += 1
                attempt_path = re.sub(r'/tr\[\d+\]', f'/tr[{index + attempt}]', slot_path)
                print('Trying path: ', attempt_path)
        
            except Exception as e:
                print('Page took too long or encounter an error', e)

        print('No slot available')

    except TimeoutError:
        print('Page took too long to load --> Refreshing...')
        driver.refresh()

    finally: 
        print('quitting driver')
        driver.quit()



try:
    # Step 5(final) : Set time of booking, usually 23:59
    # if desire to set time after midnight (0,0,0,0), need to set day + 1 on top

    # thread.start_new_thread(main, (23,59,59,6000))
    # thread.start_new_thread(main, (23,59,59,7000))
    # thread.start_new_thread(main, (23,59,59,8000))
    # thread.start_new_thread(main, (23,59,59,9000))
    thread.start_new_thread(main, (18,28,0,0))
    # thread.start_new_thread(main, (x.hour, x.minute, x.second, x.microsecond))

    ### start time open for tuning as login expected to delay

except:
    print("Error: unable to start thread")

while 1:
    pass
