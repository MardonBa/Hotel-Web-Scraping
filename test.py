from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_eight_components():
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.marriott.com/default.mi")


    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="destinationAddress.destination")
    submit_button = driver.find_element(by=By.CLASS_NAME, value="StyledFindBtn-sc-o33zur")

    text_box.send_keys("los altos")
    submit_button.click()

    driver.implicitly_wait(1)
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-SFOMV"]/div/div[2]/div/div/a')
    submit_button.click()

    driver.implicitly_wait(1)

    driver.back()

    driver.implicitly_wait(1)
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-PAORI"]/div/div[2]/div/div/a')
    submit_button.click()

    driver.implicitly_wait(1)
    driver.back()
    time.sleep(3)

test_eight_components()
print("hello world")

