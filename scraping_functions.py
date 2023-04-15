
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
def scrape_rates_by_type(soup_name, class_name):

    ## Initializing code
    prices_list = scrape_price(soup_name)

    rate_type_list = []
    member_rates = []
    normal_rates = []

    rate_types = soup_name.find_all(attrs={'class': class_name})

    for rate_type in rate_types:
        rate_type_list.append(rate_type.get_text())

    ## Cleans the data
    for i, rate_type in enumerate(rate_type_list):
        rate_type_list[i] = clean_data(rate_type)

    print(rate_type_list)
    print(len(rate_type_list), "rate type list length")
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
    

def scrape_criteria(soup_name, num_prices):
    room_name_list = []

    room_names = soup_name.find_all(attrs={'class': 'l-l-col-8 l-xl-col-8'})


    for name in room_names:
        room_name_list.append(name.get_text())

    for i, room in enumerate(room_name_list):
        room_name_list[i] = clean_data(room)
    
    print(room_name_list)
    print(len(room_name_list))
    room_type = []
    for i in range(num_prices):
        ## Code to add the room type to its own list
        ## Residence Inn Palo Alto Mountain View
        ## Removes it from the string to prevent interference with counting beds
        if "King Studio" in room_name_list[i]:
            room_name_list[i] = room_name_list[i].replace("King Studio", "")
            room_type.append("King Studio")
        if "Queen Studio" in room_name_list[i]:
            room_name_list[i] = room_name_list[i].replace("Queen Studio", "")
            room_type.append("Queen Studio")
        if "Penthouse Suite, " in room_name_list[i]:
            room_name_list[i] = room_name_list[i].replace("Penthouse Suite", "")
            room_type.append("Penthouse Suite")

        ## Aloft Palo Alto
        elif "Aloft Room" in room_name_list[i]:
            room_type.append("Aloft Room")
        elif "Breezy Guest Room" in room_name_list[i]:
            room_type.append("Breezy Guest Room")
        elif "Savvy Plus Guest Room" in room_name_list[i]:
            room_type.append("Savvy Plus Guest Room")
        elif "Junior Suite" in room_name_list[i]:
            room_type.append("Junior Suite")

        ## Residence Inn Palo Alto Los Altos
        if "Studio" in room_name_list[i]:
            room_type.append("Studio")
        if "Suite" in room_name_list[i]:
            room_type.append("Suite")

        ## Courtyard Palo Alto Los Altos, AC Hotel Palo Alto, Hotel Citrine, 
        if "Larger Guest room" in room_name_list[i]:
            room_type.append("Larger Guest Room")
        elif "Deluxe Guest room" in room_name_list[i]:
            room_type.append("Deluxe Guest room")
        elif "Guest room" in room_name_list[i]:
            room_type.append("Guest room")
        ## No need to add code for suite because it is above

    

    print(room_type)
    return room_type

