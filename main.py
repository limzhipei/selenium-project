from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "../Desktop/Web Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
date = [date.text for date in dates]

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
event = [event.text for event in events]

event_dict = {}
for n in range(len(event)):
    event_dict[n] = {
        "time": date[n],
        "name": event[n],
    }

print(event_dict)
