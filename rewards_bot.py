import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://rewards.bing.com")
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Sign in").click()
    time.sleep(2)
    driver.find_element(By.ID, "i0116").send_keys(EMAIL)
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(2)
    driver.find_element(By.ID, "i0118").send_keys(PASSWORD)
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(3)
    try:
        driver.find_element(By.ID, "idSIButton9").click()
    except:
        pass
    time.sleep(3)

    searches = ["cricket", "bollywood", "chai", "weather", "stock market", "ipl", "virat kohli", "mumbai news", "delhi metro", "indian railway"]
    for i in range(30):
        driver.get("https://www.bing.com")
        q = searches[i % len(searches)] + " " + str(random.randint(1, 100))
        driver.find_element(By.ID, "sb_form_q").send_keys(q)
        driver.find_element(By.ID, "sb_form_q").submit()
        time.sleep(random.uniform(5, 9))
    print("✅ Bot finished")
finally:
    driver.quit()
