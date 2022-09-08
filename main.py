mport time
import schedule #install this via pip
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


URL = ""
ID_NAME = "" #This is a html element to find on the webpage
TIMEFRAME = 15 #this is in Mins
WAIT_TIME = 20 #this is in seconds

def load_webpage():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(service=Service())
    try:
        driver.get(URL)
        WebDriverWait(driver, WAIT_TIME).until(
            EC.presence_of_element_located((By.ID, ID_NAME))
        )
    except:
        print("Error in loading the page at ", '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
        # can make it send email
    finally:
        driver.close()


if __name__ == "__main__":
    schedule.every(TIMEFRAME).minutes.do(load_webpage)
    while True:
        schedule.run_pending()
        time.sleep(1)
