import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
# import _thread as thread
import threading
from config import Stars_Config

# to keep browser opening after execution
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



def main(hr, min, sec, mili):

    # set target time variable
    d = Stars_Config.BOOKING_DATE
    z = datetime.datetime(d.year, d.month, d.day, hr, min, sec, mili)

    # initialise webdriver 
    driver = webdriver.Chrome(chrome_options)
    driver.get(Stars_Config.URL)

    # enter user name
    user_name_field = driver.find_element(By.ID, 'UID')
    user_name_field.send_keys(Stars_Config.USERNAME)

    button1 = driver.find_element(By.XPATH, Stars_Config.uid_submit_path)
    button1.click()

    # enter password
    pw_field = driver.find_element(By.ID, 'PW')
    pw_field.send_keys(Stars_Config.PASSWORD)

    button2 = driver.find_element(By.XPATH, Stars_Config.pw_submit_path)
    button2.click()


    # set a timeout value
    wait_page = WebDriverWait(driver, 100)

    try:
        wait_page.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tr td form input')))
        # Register Course when time is up
        while 1:
            x = datetime.datetime.today()

            # time critical task to execute only when site refreshed
            if x > z:
                # click on register button using css_selector (number of modules may affect xpath)
                button3 = driver.find_element(By.CSS_SELECTOR, 'tr td form input')
                button3.click()
                break
        
        # wait_page.until(EC.presence_of_element_located((By.XPATH, confirmation_path)))
        print("Confirmation page is fully loaded")

        # Confirm registration when page is loaded
        button4 = driver.find_element(By.XPATH, Stars_Config.confirmation_path)
        button4.click()
    except NoSuchElementException:
        print("Registration failed due to slot")

    except Exception as e:
        print("Page took too long or encounter an error", e)

    finally: 
        print('quitting driver')
        driver.quit()



#######################
#### Script Start #####
#######################

try:
    x = Stars_Config.BOOKING_TIME
    threads = []

    # opening threads at 1000ms interval 
    for i in range(Stars_Config.THREAD_COUNT):
        t = threading.Thread(target = main, args=(x.hour, x.minute, x.second, x.microsecond + (i*1000)), name=f'Thread{i}')
        threads.append(t)
        t.start()

    # wait for thread to finish
    for t in threads:
        t.join()

    print("All Threads are closed.")

except:
    print("Error: unable to start thread")
