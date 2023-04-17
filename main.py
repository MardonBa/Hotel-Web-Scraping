import scraping_functions as sf

from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


## GUI Setup Code
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

bottomframe = tk.Frame(root)
bottomframe.pack( side = tk.BOTTOM )

redbutton = tk.Button(frame, text="Red", fg="red")
redbutton.pack( side = tk.LEFT)

greenbutton = tk.Button(frame, text="green", fg="green")
greenbutton.pack( side = tk.LEFT )

bluebutton = tk.Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = tk.LEFT )

blackbutton = tk.Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = tk.BOTTOM)

root.mainloop()

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
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-SFOMV"]/div/div[2]/div/div/a/div')
        submit_button.click()

        residence_inn_palo_alto_mountain_view = driver.page_source
        residence_inn_palo_alto_mountain_view_soup = BeautifulSoup(residence_inn_palo_alto_mountain_view, "html.parser")

           

    except:
        print("error finding this element by text: ", "Residence Inn Palo Alto Mountain View")
        break

    else:
        ## Goes back to the page with hotels on it
        driver.back()

        ## Adds prices to lists
        ripamv_scraped_member_rate, ripamv_scraped_normal_rate = sf.scrape_rates_by_type(residence_inn_palo_alto_mountain_view_soup)
        for rate in ripamv_scraped_member_rate:
            member_rate.append(rate)
        for rate in ripamv_scraped_normal_rate:
            normal_rate.append(rate)

        ## Adds hotel names to lists
        for i in ripamv_scraped_member_rate:
            hotel_name.append("Residence Inn Palo Alto Mountain View")

        room_types, hotel_king_beds, hotel_queen_beds, hotel_sofa_beds, views, location_list, balcony_exists, hotel_num_rooms = sf.scrape_criteria(residence_inn_palo_alto_mountain_view_soup, len(ripamv_scraped_member_rate))
        for i in range(len(ripamv_scraped_normal_rate)):
            room_type.append(room_types[i])
            king_beds.append(hotel_king_beds[i])
            queen_beds.append(hotel_queen_beds[i])
            sofa_beds.append(hotel_sofa_beds[i])
            view.append(views[i])
            room_location.append(location_list[i])
            balcony.append(balcony_exists[i])
            num_rooms.append(hotel_num_rooms[i])
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


    except:
        print("error finding this element by XPATH: ", "Residence Inn Palo Alto Los Altos")
        break

    else:
        ## Goes back to the page with hotels on it
        driver.back()

        ## Ads prices to lists
        ripala_scraped_member_rate, ripala_scraped_normal_rate = sf.scrape_rates_by_type(residence_inn_palo_alto_los_altos_soup)
        for rate in ripala_scraped_member_rate:
            member_rate.append(rate)
        for rate in ripala_scraped_normal_rate:
            normal_rate.append(rate)


        ## Adds hotel names to lists
        for i in ripala_scraped_member_rate:
            hotel_name.append("Residence Inn Palo Alto Los Altos")

        room_types, hotel_king_beds, hotel_queen_beds, hotel_sofa_beds, views, location_list, balcony_exists, hotel_num_rooms = sf.scrape_criteria(residence_inn_palo_alto_los_altos_soup, len(ripala_scraped_member_rate))
        for i in range(len(ripala_scraped_member_rate)):
            room_type.append(room_types[i])
            king_beds.append(hotel_king_beds[i])
            queen_beds.append(hotel_queen_beds[i])
            sofa_beds.append(hotel_sofa_beds[i])
            view.append(views[i])
            room_location.append(location_list[i])
            balcony.append(balcony_exists[i])
            num_rooms.append(hotel_num_rooms[i])
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


    except:
        print("error finding this element by XPATH: ", "Courtyard Palo Alto Los Altos")
        break

    else:
        ## Goes back to the page with hotels on it
        driver.back()

        cpala_scraped_member_rate, cpala_scraped_normal_rate = sf.scrape_rates_by_type(courtyard_palo_alto_los_altos_soup)
        for rate in cpala_scraped_member_rate:
            member_rate.append(rate)
        for rate in cpala_scraped_normal_rate:
            normal_rate.append(rate)

        ## Adds hotel names to lists
        for i in cpala_scraped_member_rate:
            hotel_name.append("Courtyard Palo Alto Los Altos")

        room_types, hotel_king_beds, hotel_queen_beds, hotel_sofa_beds, views, location_list, balcony_exists, hotel_num_rooms = sf.scrape_criteria(courtyard_palo_alto_los_altos_soup, len(cpala_scraped_member_rate))
        for i in range(len(cpala_scraped_member_rate)):
            room_type.append(room_types[i])
            king_beds.append(hotel_king_beds[i])
            queen_beds.append(hotel_queen_beds[i])
            sofa_beds.append(hotel_sofa_beds[i])
            view.append(views[i])
            room_location.append(location_list[i])
            balcony.append(balcony_exists[i])
            num_rooms.append(hotel_num_rooms[i])
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


    except: 
        print("error finding this element by XPATH: ", "AC Hotel Palo Alto")
        break

    else:
        ## Goes back to the page with hotels on it
        driver.back()

        achpa_scraped_member_rate, achpa_scraped_normal_rate = sf.scrape_rates_by_type(ac_hotel_palo_alto_soup)
        for rate in achpa_scraped_member_rate:
            member_rate.append(rate)
        for rate in achpa_scraped_normal_rate:
            normal_rate.append(rate)

        ## Adds hotel names to lists
        for i in achpa_scraped_member_rate:
            hotel_name.append("AC Hotel Palo Alto")

        room_types, hotel_king_beds, hotel_queen_beds, hotel_sofa_beds, views, location_list, balcony_exists, hotel_num_rooms = sf.scrape_criteria(ac_hotel_palo_alto_soup, len(achpa_scraped_member_rate))
        for i in range(len(achpa_scraped_member_rate)):
            room_type.append(room_types[i])
            king_beds.append(hotel_king_beds[i])
            queen_beds.append(hotel_queen_beds[i])
            sofa_beds.append(hotel_sofa_beds[i])
            view.append(views[i])
            room_location.append(location_list[i])
            balcony.append(balcony_exists[i])
            num_rooms.append(hotel_num_rooms[i])
        break


## Hotel Citrine Palo Alto, a Tribute Portfolio Hotel
while True:
    ## Navigate to the page with the rooms for this hotel
    try:
        driver.implicitly_wait(1)
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-SJCTX"]/div/div[2]/div/div/a/div')
        submit_button.click()

        hotel_citrine_palo_alto = driver.page_source
        hotel_citrine_palo_alto_soup = BeautifulSoup(hotel_citrine_palo_alto, "html.parser")

    
    except:
        print("error finding this element by XPATH: ", "Hotel Citrine Palo Alto")
        break

    else:
        ## Goes back to the page with hotels on it
        driver.back()

        hcpa_scraped_member_rate, hcpa_scraped_normal_rate = sf.scrape_rates_by_type(hotel_citrine_palo_alto_soup)
        for rate in hcpa_scraped_member_rate:
            member_rate.append(rate)
        for rate in hcpa_scraped_normal_rate:
            normal_rate.append(rate)

        ## Adds hotel names to lists
        for i in hcpa_scraped_member_rate:
            hotel_name.append("Hotel Citrine Palo Alto")

        room_types, hotel_king_beds, hotel_queen_beds, hotel_sofa_beds, views, location_list, balcony_exists, hotel_num_rooms = sf.scrape_criteria(hotel_citrine_palo_alto_soup, len(hcpa_scraped_member_rate))
        for i in range(len(hcpa_scraped_member_rate)):
            room_type.append(room_types[i])
            king_beds.append(hotel_king_beds[i])
            queen_beds.append(hotel_queen_beds[i])
            sofa_beds.append(hotel_sofa_beds[i])
            view.append(views[i])
            room_location.append(location_list[i])
            balcony.append(balcony_exists[i])
            num_rooms.append(hotel_num_rooms[i])
        break


## Aloft Mountain View
while True:
    ## Navigate to the page with the rooms for this hotel
    try:
        driver.implicitly_wait(1)
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="property-record-map-SJCAM"]/div/div[2]/div/div/a/div')
        submit_button.click()

        ## Code to navigate from deals to standard prices
        driver.implicitly_wait(1)
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="ui-id-1"]/span[1]')
        submit_button.click()
        

        aloft_mountain_view = driver.page_source
        aloft_mountain_view_soup = BeautifulSoup(aloft_mountain_view, "html.parser")
        
    
    except:
        print("error finding this element by XPATH: ", "Aloft Mountain View")
        break

    else:
        amv_scraped_member_rate, amv_scraped_normal_rate = sf.scrape_rates_by_type(aloft_mountain_view_soup)
        for rate in amv_scraped_member_rate:
            member_rate.append(rate)
        for rate in amv_scraped_normal_rate:
            normal_rate.append(rate)

        ## Adds hotel names to lists
        for i in amv_scraped_member_rate:
            hotel_name.append("Aloft Mountain View")

        room_types, hotel_king_beds, hotel_queen_beds, hotel_sofa_beds, views, location_list, balcony_exists, hotel_num_rooms = sf.scrape_criteria(aloft_mountain_view_soup, len(amv_scraped_member_rate))
        
        print(room_types)
        print(len(room_types))
        print(len(amv_scraped_member_rate))
        for i in range(len(amv_scraped_member_rate)):
            room_type.append(room_types[i])
            king_beds.append(hotel_king_beds[i])
            queen_beds.append(hotel_queen_beds[i])
            sofa_beds.append(hotel_sofa_beds[i])
            view.append(views[i])
            room_location.append(location_list[i])
            balcony.append(balcony_exists[i])
            num_rooms.append(hotel_num_rooms[i])
        break
driver.close()


dict = {
    'Member Rate': member_rate,
    'Normal Rate': normal_rate,
    'Hotel Name': hotel_name,
    'Room Type': room_type,
    'Num. King Beds': king_beds,
    'Num. Queen Beds': queen_beds,
    'Num. Sofa Beds': sofa_beds,
    'View': view,
    'Room Location': room_location,
    'Balcony': balcony,
    'Num. Rooms': num_rooms
}

df = pd.DataFrame(dict)
pd.set_option('display.max_columns', None)
print(df.to_string())

