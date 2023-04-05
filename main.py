from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import time

# Selenium import and setup code
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Initiates the web driver
# Options = options is to hide the browser, not necessary until final product
driver = webdriver.Chrome(service=service)

# Loads the Marriott link the the browser
driver.get("https://www.marriott.com/default.mi")


driver.implicitly_wait(0.5)

## Navigates the page with the hotels on it
text_box = driver.find_element(by=By.NAME, value="destinationAddress.destination")
submit_button = driver.find_element(by=By.CLASS_NAME, value="StyledFindBtn-sc-o33zur")

text_box.send_keys("los altos")
submit_button.click()


## Setup code for BeautifulSoup scraping
## Saving webpages to their respective variables using driver.page_source
## Then creating a BeautifulSoup instance title webpagename_soup

## Residence Inn Palo Alto Mountain Viewx
## Navigates to the page with rooms for this hotel
driver.implicitly_wait(1)
submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-SFOMV"]/div/div[2]/div/div/a')
submit_button.click()

residence_inn_palo_alto_mountain_view = driver.page_source
residence_inn_palo_alto_mountain_view_soup = BeautifulSoup(residence_inn_palo_alto_mountain_view, "html.parser")

## Goes back to the page with hotels on it
driver.back() 


## Residence Inn Palo Alto Los Altos
## Navigates to the page with rooms for this hotel
driver.implicitly_wait(1)
submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-PAORI"]/div/div[2]/div/div/a')
submit_button.click()

residence_inn_palo_alto_los_altos = driver.page_source
residence_inn_palo_alto_los_altos_soup = BeautifulSoup(residence_inn_palo_alto_los_altos, "html.parser")

## Goes back to the page with hotels on it
driver.back()


## Courtyard Palo Alto Los Altos
## Navigate to the page with rooms for this hotel
driver.implicitly_wait(1)
submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-PAOCY"]/div/div[2]/div/div/a')
submit_button.click()

courtyard_palo_alto_los_altos = driver.page_source
courtyard_palo_alto_los_altos_soup = BeautifulSoup(courtyard_palo_alto_los_altos, "html.parser")

## Goes back to the page with the hotels on it
driver.back()


## AC Hotel Palo Alto
## Navigate to the page with rooms for this hotel
driver.implicitly_wait(1)
submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-SJCAO"]/div/div[2]/div/div/a')
submit_button.click()

ac_hotel_palo_alto = driver.page_source
ac_hotel_palo_alto_soup = BeautifulSoup(ac_hotel_palo_alto, "html.parser")

## Goes back to the page with the hotels on it
driver.back()


## Hotel Citrine Palo Alto, a Tribute Portfolio Hotel
## Navigate to the page with the rooms for this hotel
driver.implicitly_wait(1)
submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-SJCTX"]/div/div[2]/div/div/a')
submit_button.click()

hotel_citrine_palo_alto = driver.page_source
hotel_citrine_palo_alto_soup = BeautifulSoup(hotel_citrine_palo_alto, "html.parser")

## Goes back to the page with the hotels on it
driver.back()


## Aloft Mountain View
## Navigate to the page with thr rooms for this hotel
driver.implicitly_wait(1)
submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-SJCAM"]/div/div[2]/div/div/a')
submit_button.click()
time.sleep(5)

aloft_mountain_view = driver.page_source
aloft_mountain_view_soup = BeautifulSoup(aloft_mountain_view, "html.parser")