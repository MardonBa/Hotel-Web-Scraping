
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
    

def scrape_room_types(room_name_list, num_prices):
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

        ## Residence Inn Palo Alto
        if "Studio" in room_name_list[i]:
            room_type.append("Studio")
        if "Suite" in room_name_list[i]:
            room_type.append("Suite")
        
        ## Courtyard Palo Alto Los Altos, AC Hotel Palo Alto, Hotel Citrine 
        if "Guest room" in room_name_list[i]:
            room_type.append("Guest room")
        if "Larger Guest room" in room_name_list[i]:
            room_type.append("Larger Guest room")
        if "Deluxe Guest room" in room_name_list[i]:
            room_type.append("Deluxe Guest room")

        ## Aloft Palo Alto
        elif "Aloft Room" in room_name_list[i]:
            room_type.append("Aloft Room")
        elif "Breezy Guest Room" in room_name_list[i]:
            room_type.append("Breezy Guest Room")
        elif "Savvy Plus Guest Room" in room_name_list[i]:
            room_type.append("Savvy Plus Guest Room")
        elif "Junior Suite" in room_name_list[i]:
            room_type.append("Junior Suite")

    return room_type, room_name_list        ## room_name_list is returned so that the strings that would interfere in Residence Inn Palo Alto Mountain View don't affect later code

def scrape_beds(room_name_list, num_prices):
    king_beds = []
    queen_beds = []
    sofa_beds = []
    print(room_name_list)
    for i in range(num_prices):
        ## Code to add the number of each bed to its respective list
        ## N/A if a bed type is not in the room
        if "King" in room_name_list[i]:
            king_index = room_name_list[i].index("King")
            king_beds.append(int(room_name_list[i][king_index -  2]))
        else: 
            king_beds.append("N/A")

        if "Queen" in room_name_list[i]:
            queen_index = room_name_list[i].index("Queen")
            print(queen_index)
            queen_beds.append(int(room_name_list[i][queen_index - 2]))
        else: 
            queen_beds.append("N/A")

        if "Sofa bed" in room_name_list[i]:
            sofa_beds.append(1)
        else:
            sofa_beds.append("N/A")
        

    return king_beds, queen_beds, sofa_beds



    

def scrape_criteria(soup_name, num_prices):
    room_name_list = []
    room_names = soup_name.find_all(attrs={'class': 'l-l-col-8 l-xl-col-8'})
    for name in room_names:
        room_name_list.append(name.get_text())
    ## Cleans the data
    for i, room in enumerate(room_name_list):
        room_name_list[i] = clean_data(room)

    

    room_type, new_room_name_list = scrape_room_types(room_name_list, num_prices)
    king_beds, queen_beds, sofa_beds = scrape_beds(new_room_name_list, num_prices)

    

    print(room_type)
    return room_type, king_beds, queen_beds, sofa_beds

