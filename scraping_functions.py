
import re

def clean_data(data, data_type=None):
    return_data = data.strip()
    if data_type != None:
        return_data = data_type(data)
    return return_data


def scrape_price(soup_name):
    prices_list = []
    prices = soup_name.find_all(attrs={'class': "t-font-xl l-display-inline-block l-margin-none t-font-weight-bold"})
    for price in prices:
        prices_list.append(price.get_text())

    ## Cleans the data
    for i, price in enumerate(prices_list):
        prices_list[i] = clean_data(price, int)


    return prices_list

## soup_name should be the BeautifulSoup instance for the hotel, class_name should be a css class as a string
def scrape_rates_by_type(soup_name):

    ## Initializing code
    prices_list = scrape_price(soup_name)

    rate_type_list = []
    member_rates = []
    normal_rates = []

    rate_types = soup_name.find_all(attrs={'class': 'description t-description l-margin-none t-font-ml t-line-height-xxl t-font-m'})

    for rate_type in rate_types:
        rate_type_list.append(rate_type.get_text())

    ## Cleans the data
    for i, rate_type in enumerate(rate_type_list):
        rate_type_list[i] = clean_data(rate_type)

    ## Code to add the rate to member or normal rates
    for i, rate_type in enumerate(rate_type_list):
        rate_type = rate_type_list[i]
        if rate_type == "Flexible Rate":
            normal_rates.append(prices_list[i])
            try:            ## accounts for if testing the last term in the list
                if i == 0:              ## accounts for if there is no member rate on the first room listed
                    member_rates.append("N/A")
                if rate_type_list[i + 1] == "Flexible Rate":
                    member_rates.append("N/A")
            except: break
        else:
            member_rates.append(prices_list[i])

    return member_rates, normal_rates
    

def scrape_room_types(room_name_list, num_prices, member_rates, normal_rates, hotel_name):
    room_type = []
    ## Check the room name against the list of all real room names
    ## if there is a room name in the actual list not in the scraped list make the rates SOLD OUT
    ## if there is a room name that is in the scraped list and noy in the actual list add the rate as normal
    ripamv_room_types = ["Queen Studio, Studio, 1 Queen(s), Sofa bed", "King Studio, Studio, 1 King, Sofa bed", "Penthouse Suite, Bedroom 1(Loft): 1 Queen(s), Bedroom 2: 1 Queen(s), Sofa bed"]
    ripala_room_types = ["Studio, 1 Queen(s), Sofa bed", "1 Bedroom Suite, 1 Queen(s), Sofa bed", "2 Bedroom Suite, Bedroom 1: 1 Queen(s), Bedroom 2: 1 Queen(s), Sofa bed"]
    cpala_room_types =  ["Guest room, 1 King, Sofa bed", "Guest room, 2 Queen(s)", "Larger Guest room, 1 King, Sofa bed", "Larger Guest room, 2 Queen(s), Sofa bed", "1 Bedroom 2 room Suite, 1 King, Sofa bed", "1 Bedroom 2 room Suite, 2 Queen(s), Sofa bed, Courtyard view"]
    achpa_room_types = ["Guest room, 1 King", "Guest room, 2 Queen(s)", "Guest room, 1 King, Mountain view", "Guest room, 2 Queen(s), Mountain view", "Guest room, 1 King, Corner room", "Deluxe Guest room, 1 King", "Deluxe Guest room, 1 King, Mountain view, Balcony"]
    hcpa_room_types =  ["Guest room, 1 King", "Guest room, 2 Queen(s)", "Guest room, 1 King, High floor", "Guest room, 2 Queen(s), High floor", "Deluxe Guest room, 1 King, Balcony", "Deluxe Guest room, 2 Queen(s), City view, Balcony", "1 Bedroom Suite, 1 King, Sofa bed", "Suite, Bedroom 1: 1 King, Bedroom 2: 2 Doubles, Sofa bed"]
    amv_room_types = ["1 King Bed, Aloft Room", "1 King Bed, High Floor, Breezy Guest Room", "1 King Bed, Pool View, Aloft Room", "1 King Bed, Savvy Guest Room", "2 King Beds, Aloft Room", "1 King Bed, Pool View, High Floor, Breezy Guest Room", "1 King Bed, Corner, Junior Suite"]

    if hotel_name == "ripamv":
        for i, room_name in enumerate(ripamv_room_types):
            print("room name being checked:", room_name)
            try:
                if room_name_list[i] != room_name:
                    print("original room_name_list[i]:", room_name_list[i])
                    member_rates.insert(i, "SOLD OUT") 
                    normal_rates.insert(i, "SOLD OUT")
                    room_name_list.insert(i, "placeholder")     ## Placeholder so that all the future values don't get messed up
                    print("new room_name_list[i]", room_name_list[i])
            except IndexError:
                member_rates.append("SOLD OUT")
                normal_rates.append("SOLD OUT")

        room_name_list = ripamv_room_types      ## Used to set the list of room names to get the room types
    elif hotel_name == "ripala":
        for i, room_name in enumerate(ripala_room_types):
            print("room name being checked:", room_name)
            try:
                if room_name_list[i] != room_name:
                    member_rates.insert(i, "SOLD OUT") 
                    normal_rates.insert(i, "SOLD OUT")
                    room_name_list.insert(i, "placeholder")     ## Placeholder so that all the future values don't get messed up
            except IndexError:
                member_rates.append("SOLD OUT")
                normal_rates.append("SOLD OUT")
        room_name_list = ripala_room_types      ## Used to set the list of room names to get the room types
    elif hotel_name == "cpala":
        for i, room_name in enumerate(cpala_room_types):
            print("room name being checked:", room_name)
            try:
                if room_name_list[i] != room_name:
                    member_rates.insert(i, "SOLD OUT") 
                    normal_rates.insert(i, "SOLD OUT")
                    room_name_list.insert(i, "placeholder")     ## Placeholder so that all the future values don't get messed up
            except IndexError:
                member_rates.append("SOLD OUT")
                normal_rates.append("SOLD OUT")
        room_name_list = cpala_room_types      ## Used to set the list of room names to get the room types
    elif hotel_name == "achpa":
        for i, room_name in enumerate(achpa_room_types):
            print("room name being checked:", room_name)
            try:
                if room_name_list[i] != room_name:
                    member_rates.insert(i, "SOLD OUT") 
                    normal_rates.insert(i, "SOLD OUT")
                    room_name_list.insert(i, "placeholder")     ## Placeholder so that all the future values don't get messed up
            except IndexError:
                member_rates.append("SOLD OUT")
                normal_rates.append("SOLD OUT")
        room_name_list = achpa_room_types      ## Used to set the list of room names to get the room types
    elif hotel_name == "hcpa":
        for i, room_name in enumerate(hcpa_room_types):
            print("room name being checked:", room_name)
            try:
                if room_name_list[i] != room_name:
                    member_rates.insert(i, "SOLD OUT") 
                    normal_rates.insert(i, "SOLD OUT")
                    room_name_list.insert(i, "placeholder")     ## Placeholder so that all the future values don't get messed up
            except IndexError:
                member_rates.append("SOLD OUT")
                member_rates.append("SOLD OUT")
        room_name_list = hcpa_room_types      ## Used to set the list of room names to get the room types
    elif hotel_name == "amv":
        for i, room_name in enumerate(amv_room_types):
            print("room name being checked:", room_name)
            try:
                if room_name_list[i] != room_name:
                    member_rates.insert(i, "SOLD OUT") 
                    member_rates.insert(i, "SOLD OUT")
                    room_name_list.insert(i, "placeholder")     ## Placeholder so that all the future values don't get messed up
            except IndexError:
                member_rates.append("SOLD OUT")
                member_rates.append("SOLD OUT")
        room_name_list = amv_room_types      ## Used to set the list of room names to get the room types

    for i in range(num_prices):
        ## Code to add the room type to its own list
        ## Residence Inn Palo Alto Mountain View
        ## Removes it from the string to prevent interference with counting beds
        if "King Studio" in room_name_list[i]:
            room_name_list[i] = room_name_list[i].replace("King Studio", "")
            room_type.append("King Studio")
        elif "Queen Studio" in room_name_list[i]:
            room_name_list[i] = room_name_list[i].replace("Queen Studio", "")
            room_type.append("Queen Studio")
        elif "Penthouse Suite, " in room_name_list[i]:
            room_name_list[i] = room_name_list[i].replace("Penthouse Suite", "")
            room_type.append("Penthouse Suite")
        
        ## Aloft Palo Alto
        elif "Aloft Room" in room_name_list[i]:
            room_type.append("Aloft Room")
        elif "Breezy Guest Room" in room_name_list[i]:
            room_type.append("Breezy Guest Room")
        elif "Savvy Guest Room" in room_name_list[i]:
            room_type.append("Savvy Guest Room")
        elif "Savvy Plus Guest Room" in room_name_list[i]:
            room_type.append("Savvy Plus Guest Room")
        elif "Junior Suite" in room_name_list[i]:
            room_type.append("Junior Suite")

        ## Residence Inn Palo Alto Los Altos
        elif "Studio" in room_name_list[i]:
            room_type.append("Studio")
        elif "2 Bedroom Suite" in room_name_list[i]:
            room_type.append("2 Bedroom Suite")
        elif "Suite" in room_name_list[i]:
            room_type.append("Suite")
        
        ## Courtyard Palo Alto Los Altos, AC Hotel Palo Alto, Hotel Citrine 
        elif "Larger Guest room" in room_name_list[i]:
            room_type.append("Larger Guest room")
        elif "Deluxe Guest room" in room_name_list[i]:
            room_type.append("Deluxe Guest room")
        elif "Guest room" in room_name_list[i]:
            room_type.append("Guest room")
        


    return room_type, room_name_list, member_rates, normal_rates        ## room_name_list is returned so that the strings that would interfere in Residence Inn Palo Alto Mountain View don't affect later code

def scrape_beds(room_name_list, num_prices):
    king_beds = [0 for i in range(num_prices)]
    queen_beds = [0 for i in range(num_prices)]
    sofa_beds = [0 for i in range(num_prices)]
    for i in range(num_prices):
        ## Code to add the number of each bed to its respective list
        ## N/A if a bed type is not in the room
        if "King" in room_name_list[i]:
            for string in re.finditer("King", room_name_list[i]):
                king_index = string.start()
                king_beds[i] += int(room_name_list[i][king_index -  2])
        else: 
            king_beds[i] = "N/A"

        if "Queen" in room_name_list[i]:
            for string in re.finditer("Queen", room_name_list[i]):
                queen_index = string.start()
                queen_beds[i] += int(room_name_list[i][queen_index -  2])
        else: 
            queen_beds[i] ="N/A"

        if "Sofa bed" in room_name_list[i]:
            sofa_beds[i] = 1
        else:
            sofa_beds[i] = "N/A"
        

    return king_beds, queen_beds, sofa_beds

def scrape_view(room_name_list, num_prices):
    views = []
    for i in range(num_prices):
        if "Courtyard view" in room_name_list[i]:
            views.append("Courtyard view")
        elif "Mountain view" in room_name_list[i]:
            views.append("Mountain view")
        elif "Pool View" in room_name_list[i]:
            views.append("Pool View")
        else:
            views.append("N/A")

    return views

def scrape_room_location(room_name_list, num_prices):
    location_list = []
    for i in range(num_prices):
        if "High Floor" in room_name_list[i].title():
            location_list.append("High Floor")
        elif "Corner room" in room_name_list[i]:
            location_list.append("Corner")
        elif "Corner" in room_name_list[i]:
            location_list.append("Corner")
        else:
            location_list.append("N/A")

    return location_list

def scrape_balcony(room_name_list, num_prices):
    balcony_list = []
    for i in range(num_prices):
        if "Balcony" in room_name_list[i]:
            balcony_list.append(True)
        else:
            balcony_list.append(False)

    return balcony_list

def scrape_criteria(soup_name, num_prices, member_rates, normal_rates, hotel_name):
    room_name_list = []
    room_names = soup_name.find_all(attrs={'class': 'l-l-col-8 l-xl-col-8'})
    for name in room_names:
        room_name_list.append(name.get_text())
    ## Cleans the data
    for i, room in enumerate(room_name_list):
        room_name_list[i] = clean_data(room)

    

    room_type, new_room_name_list, member_rate, normal_rate = scrape_room_types(room_name_list, num_prices, member_rates, normal_rates, hotel_name)
    king_beds, queen_beds, sofa_beds = scrape_beds(new_room_name_list, num_prices)
    views = scrape_view(room_name_list, num_prices)
    location_list = scrape_room_location(room_name_list, num_prices)
    balcony = scrape_balcony(room_name_list, num_prices)
    

    return room_type, king_beds, queen_beds, sofa_beds, views, location_list, balcony, member_rate, normal_rate

