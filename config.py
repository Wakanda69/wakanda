from datetime import time
from datetime import date
from credentials import Credentials

class Stars_Config:
    # change booking time here 
    BOOKING_TIME = time(14,00,00,0000)
    BOOKING_DATE = date.today()
    THREAD_COUNT = 1

    USERNAME = Credentials.USERNAME_JANICE
    PASSWORD = Credentials.PASSWORD_JANICE

    ### ]Specify exact paths for the booking (retrieve using XPATH) ###
    URL = "https://wish.wis.ntu.edu.sg/pls/webexe/ldap_login.login?w_url=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_planner.main"

    uid_submit_path = '//*[@id="top"]/div/section[2]/div/div/center[1]/form/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input[1]'

    pw_submit_path = '//*[@id="top"]/div/section[2]/div/div/form/center[1]/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]'

    # register_path may vary depending on the number of modules planned, recommend css_selector
    register_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr[1]/td[2]/table/tbody/tr[12]/td/form/input[1]'

    confirmation_path = '//*[@id="top"]/div/section[2]/div/div/input[1]'

