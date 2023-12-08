from datetime import time
from datetime import date
from credentials import Credentials

class Stars_Config:
    # change booking time here 
    BOOKING_TIME = time(14,00,00,0000)
    BOOKING_DATE = date.today()
    START_TIME = time(13,59,0,0)
    THREAD_COUNT = 3

    USERNAME = Credentials.USERNAME_JANICE
    PASSWORD = Credentials.PASSWORD_JANICE

    ### Specify exact paths for the booking (retrieve using XPATH) ###
    URL = "https://wish.wis.ntu.edu.sg/pls/webexe/ldap_login.login?w_url=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_planner.main"

    uid_submit_path = '//*[@id="top"]/div/section[2]/div/div/center[1]/form/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input[1]'

    pw_submit_path = '//*[@id="top"]/div/section[2]/div/div/form/center[1]/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]'

    # register_path may vary depending on the number of modules planned, recommend css_selector
    register_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr[1]/td[2]/table/tbody/tr[12]/td/form/input[1]'

    confirmation_path = '//*[@id="top"]/div/section[2]/div/div/input[1]'


class Src_Config():
    # change booking time here
    BOOKING_TIME = time(10,29,0,0)
    BOOKING_DATE = date.today() # +1 if booking on midnight
    START_TIME = time(10,29,0,0)
    THREAD_COUNT = 1
    MAX_ATTEMPT = 10

    USERNAME = Credentials.USERNAME_JANICE + '@student'
    PASSWORD = Credentials.PASSWORD_JANICE


    ### Specify exact paths for the booking (retrieve using XPATH), UNCOMMENT the sports desired ###
    ### The slot path can be modify tr -> row, td -> col ###
    ### Badminton ###
    booking_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/ul/li[4]/table[2]/tbody/tr[1]/td/input'
    slot_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[7]/td[9]/input'

    ### Gym ###
    # booking_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/ul/li[4]/table[2]/tbody/tr[6]/td/input'
    # slot_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[10]/td[2]/input'


    ### Constants ###
    URL = "https://venus2.wis.ntu.edu.sg/ADFSSSO2/User/Login.aspx?app=https://wis.ntu.edu.sg/pls/webexe88/srce_smain_s.Notice_O"
    confirmation_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/input[18]'
    page_path = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form'
