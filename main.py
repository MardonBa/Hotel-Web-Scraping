import scraping_functions as sf

from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import time

# Selenium import and setup code
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('headless')

# Initiates the web driver
# Options = options is to hide the browser, not necessary until final product
driver = webdriver.Chrome()

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

## Creating the lists for every criteria as well as prices to be later put in a DataFrame
hotel_name = []
king_beds = []
queen_beds = []
sofa_beds = []
view = []
room_type = []
room_location = []
num_rooms = []
balcony = []
normal_rate = []
member_rate = []
prepaid_normal_rate = []
prepaid_member_rate = []

## Residence Inn Palo Alto Mountain View
while True:
    ## Navigates to the page with rooms for this hotel
    try:
        driver.implicitly_wait(1)
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-SFOMV"]/div/div[2]/div/div/a')
        submit_button.click()

        residence_inn_palo_alto_mountain_view = driver.page_source
        residence_inn_palo_alto_mountain_view_soup = BeautifulSoup(residence_inn_palo_alto_mountain_view, "html.parser")

        ## Goes back to the page with hotels on it
        driver.back()
           

    except:
        print("error finding this element by text: ", "Residence Inn Palo Alto Mountain View")
        break

    else:
        member_rate, normal_rate = sf.scrape_rates_by_type(residence_inn_palo_alto_mountain_view_soup, "description t-description l-margin-none t-font-ml t-line-height-xxl t-font-m")
        print("member rates: ", member_rate)
        print("normal rates: ", normal_rate)
        break


## Residence Inn Palo Alto Los Altos
while True:
    ## Navigates to the page with rooms for this hotel
    try:
        driver.implicitly_wait(1)
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-PAORI"]/div/div[2]/div/div/a')
        submit_button.click()

        residence_inn_palo_alto_los_altos = driver.page_source
        residence_inn_palo_alto_los_altos_soup = BeautifulSoup(residence_inn_palo_alto_los_altos, "html.parser")

        ## Goes back to the page with hotels on it
        driver.back()


    except:
        print("error finding this element by XPATH: ", "Residence Inn Palo Alto Los Altos")
        break

    else:
        member_rate, normal_rate = sf.scrape_rates_by_type(residence_inn_palo_alto_los_altos_soup, "description t-description l-margin-none t-font-ml t-line-height-xxl t-font-m")
        print("member rates: ", member_rate)
        print("normal rates: ", normal_rate)
        break


## Courtyard Palo Alto Los Altos
while True:
    ## Navigate to the page with rooms for this hotel
    try:
        driver.implicitly_wait(1)
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-PAOCY"]/div/div[2]/div/div/a')
        submit_button.click()

        courtyard_palo_alto_los_altos = driver.page_source
        courtyard_palo_alto_los_altos_soup = BeautifulSoup(courtyard_palo_alto_los_altos, "html.parser")

        ## Goes back to the page with the hotels on it
        driver.back()

    except:
        print("error finding this element by XPATH: ", "Courtyard Palo Alto Los Altos")
        break

    else:
        member_rate, normal_rate = sf.scrape_rates_by_type(courtyard_palo_alto_los_altos_soup, "description t-description l-margin-none t-font-ml t-line-height-xxl t-font-m")
        print("member rates: ", member_rate)
        print("normal rates: ", normal_rate)
        break


## AC Hotel Palo Alto
while True:
    try:
        ## Navigate to the page with rooms for this hotel
        driver.implicitly_wait(1)
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-SJCAO"]/div/div[2]/div/div/a')
        submit_button.click()

        ac_hotel_palo_alto = driver.page_source
        ac_hotel_palo_alto_soup = BeautifulSoup(ac_hotel_palo_alto, "html.parser")

        ## Goes back to the page with the hotels on it
        driver.back()
    
    except: 
        print("error finding this element by XPATH: ", "AC Hotel Palo Alto")
        break

    else:
        member_rate, normal_rate = sf.scrape_rates_by_type(ac_hotel_palo_alto_soup, "description t-description l-margin-none t-font-ml t-line-height-xxl t-font-m")
        print("member rates: ", member_rate)
        print("normal rates: ", normal_rate)
        break


## Hotel Citrine Palo Alto, a Tribute Portfolio Hotel
while True:
    ## Navigate to the page with the rooms for this hotel
    try:
        driver.implicitly_wait(1)
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-SJCTX"]/div/div[2]/div/div/a')
        submit_button.click()

        hotel_citrine_palo_alto = driver.page_source
        hotel_citrine_palo_alto_soup = BeautifulSoup(hotel_citrine_palo_alto, "html.parser")

        ## Goes back to the page with the hotels on it
        driver.back()
    
    except:
        print("error finding this element by XPATH: ", "Hotel Citrine Palo Alto")
        break

    else:
        member_rate, normal_rate = sf.scrape_rates_by_type(hotel_citrine_palo_alto_soup, "description t-description l-margin-none t-font-ml t-line-height-xxl t-font-m")
        print("member rates: ", member_rate)
        print("normal rates: ", normal_rate)
        break


## Aloft Mountain View
while True:
    ## Navigate to the page with the rooms for this hotel
    try:
        driver.implicitly_wait(1)
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-SJCAM"]/div/div[2]/div/div/a')
        submit_button.click()

        ## Code to navigate from deals to standard prices
        driver.implicitly_wait(1)
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="ui-id-1"]/span[1]')
        submit_button.click()
        

        aloft_mountain_view = driver.page_source
        aloft_mountain_view_soup = BeautifulSoup(aloft_mountain_view, "html.parser")

        time.sleep(5)
        
    
    except:
        print("error finding this element by XPATH: ", "Aloft Mountain View")
        break

    else:
        member_rate, normal_rate = sf.scrape_rates_by_type(aloft_mountain_view_soup, "description t-description l-margin-none t-font-ml t-line-height-xxl t-font-m")
        print("member rates: ", member_rate)
        print("normal rates: ", normal_rate)
        break