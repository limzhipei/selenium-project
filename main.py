from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = "../Desktop/Web Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")

element_ids = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment",
               "buyAlchemy lab", "buyPortal", "buyTime machine"]


def get_moni():
    moni1 = driver.find_element(By.CSS_SELECTOR, "#buyCursor b")
    moni2 = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
    moni3 = driver.find_element(By.CSS_SELECTOR, "#buyFactory b")
    moni4 = driver.find_element(By.CSS_SELECTOR, "#buyMine b")
    moni5 = driver.find_element(By.CSS_SELECTOR, "#buyShipment b")
    moni6 = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')
    moni7 = driver.find_element(By.CSS_SELECTOR, "#buyPortal b")
    moni8 = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')

    moni_preprocess = [moni1.text.split()[2].replace(",", ""), moni2.text.split()[2].replace(",", ""),
                       moni3.text.split()[2].replace(",", ""), moni4.text.split()[2].replace(",", ""),
                       moni5.text.split()[2].replace(",", ""), moni6.text.split()[3].replace(",", ""),
                       moni7.text.split()[2].replace(",", ""), moni8.text.split()[3].replace(",", "")]

    moni_master = [int(num) for num in moni_preprocess]
    return moni_master


def upgrade():
    moni = get_moni()
    element_id_classes = []
    elements = []
    for element_id in element_ids:
        element = driver.find_element(By.ID, element_id)
        elements.append(element)
        element_id_class = element.get_attribute("class")
        element_id_classes.append(element_id_class)

    for n in range(len(element_id_classes)):
        if element_id_classes[n] == "grayed":
            moni[n] = 0
    moni_index = moni.index(max(moni))
    elements[moni_index].click()


timeout = time.time() + 60 * 5
upgrade_time = time.time() + 1
extension = 1
counter = 0

game_on = True

while game_on:
    if time.time() > timeout:
        game_on = False
    cookie.click()
    if time.time() > upgrade_time:
        upgrade()
        print("upgrade")
        upgrade_time = time.time() + 1 + extension
        if counter > 15:
            extension -= 1
        else:
            extension += 1
        counter += 1


cps = driver.find_element(By.ID, "cps")
score = cps.text.split()[2]
print(f"cookies/second : {score}")
