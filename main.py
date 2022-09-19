import logging
import time
import schedule
import datetime
import chromedriver_autoinstaller
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


URL = ""  # this is the URL the webdriver loads
ID_NAME = ""  # This is the ID (of a HTML element) that the server will wait till it finds before closing the webdriver
TIMEFRAME = 15  # This is the timeframe between loading the webpage. IT IS IN MINUTES
WAIT_TIME = 25  # this is in seconds
PATH = ""  # this is the PATH you want to save the file
FILE_NAME = "output.csv"  # this is the file name. It has to be a CSV.


def main():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(service=Service())
    try:
        start = time.time()
        driver.get(URL)
        WebDriverWait(driver, WAIT_TIME).until(
            expected_conditions.presence_of_element_located((By.ID, ID_NAME))
        )
        end = time.time()
        run_time = round(end - start, 1)
        logging.INFO(f"Loading page took {run_time}")
    except TimeoutException:
        logging.warning(f"Error in loading the page")
    finally:
        driver.close()

if __name__ == "__main__":
    logging.basicConfig(filename=os.path.join(PATH, "loading_logs.log"), level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    schedule.every(TIMEFRAME).minutes.do(main)
    main()
    while True:
        schedule.run_pending()
        time.sleep(1)
