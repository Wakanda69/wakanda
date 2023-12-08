from datetime import datetime
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re
import threading
import time
import schedule
from config import Src_Config

# to keep browser opening after execution
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


### Main Function ###
def main(hr, min, sec, mili):
    d = Src_Config.BOOKING_DATE
    z = datetime(d.year, d.month, d.day, hr, min, sec, mili)

    # initialise webdriver 
    ## fixed 26/8/2023, chromedriver version 116
    # service = Service(executable_path = 'C:/Users/teoji/Selenium/chromedriver/chromedriver.exe')
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service = service, options = options)
    driver = webdriver.Chrome(chrome_options)
    driver.get(Src_Config.URL)

    # pass the basic authentication using src url (deprecated)
    # login_URL = "https://" + user_name + ":" + password + "@" + driver.current_url[8:]
    # driver.get(login_URL)

    # new login method (updated 29/07/2023)
    # enter user name
    user_name_field = driver.find_element(By.ID, 'userNameInput')
    user_name_field.send_keys(Src_Config.USERNAME)

    # Enter password
    password_field = driver.find_element(By.ID, 'passwordInput')
    password_field.send_keys(Src_Config.PASSWORD)

    # Login
    login_button = driver.find_element(By.ID, 'submitButton')
    login_button.click()
    
    ### Determine whether page is loaded

    # set a timeout value
    wait_page = WebDriverWait(driver, 10)
    # set attempt limit for alternative slots 
    attempt = 0 
    max_attempts = Src_Config.MAX_ATTEMPT
    # find index value using regular expression (RE)
    match = re.search(r'/tr\[(\d+)\]', Src_Config.slot_path)
    if match: 
        index = int(match.group(1))
    else: 
        print('Index not found in Slot Path')
        exit()

    try:
        while 1:
            x = datetime.today()

            if x >= z:
                print('time is up')
                button1 = driver.find_element(By.XPATH, Src_Config.booking_path)
                button1.click()
                break

        # wait for document.readyState to be 'complete'
        wait_page.until(EC.presence_of_element_located((By.XPATH, Src_Config.page_path)))
        # attempt to book slot
        attempt_path = Src_Config.slot_path

        while attempt < max_attempts:
            try: 
                # throw exception if slot not available
                button2 = driver.find_element(By.XPATH, attempt_path)
                # if slot is available
                print('Slot is Available!')
                button2.click()

                # wait until slot confirmation page is loaded
                wait_page.until(EC.presence_of_element_located((By.XPATH, Src_Config.confirmation_path)))
                print('Confirmation page is fully loaded')

                # confirming slot
                button3 = driver.find_element(By.XPATH, Src_Config.confirmation_path)
                button3.click()
                print('Slot booked succesfully!')
                break

            except NoSuchElementException:
                print('Slot is not available')
                # try other slot 
                attempt += 1
                attempt_path = re.sub(r'/tr\[\d+\]', f'/tr[{index + attempt}]', Src_Config.slot_path)
                print('Trying path: ', attempt_path)
        
            except Exception as e:
                print('Page took too long or encounter an error', e)


    except TimeoutError:
        print('Page took too long to load --> Refreshing...')
        driver.refresh()

    finally: 
        print('quitting driver')
        driver.quit()

def start_threads():

    x = Src_Config.BOOKING_TIME
    threads = []

    # opening threads at 1000ms interval
    for i in range(Src_Config.THREAD_COUNT):
        t = threading.Thread(target = main, args=(x.hour, x.minute, x.second, x.microsecond + (i*1000)), name=f'Thread{i}')
        threads.append(t)
        t.start()

    # wait for threads to finish
    for t in threads:
        t.join()

    print("All Threads are closed.")
    global exit_flag
    exit_flag = True



#######################
#### Script Start #####
#######################

try:
    # global variable to terminate script
    exit_flag = False

    # set the target time
    target_time = Src_Config.START_TIME

    # schedule the start_threads function
    schedule.every().day.at(str(target_time)).do(start_threads)

    while not exit_flag:
        schedule.run_pending()
        time.sleep(1)

    print("Exiting the script.")


except Exception as e:
    print(f'Error: {e}')
