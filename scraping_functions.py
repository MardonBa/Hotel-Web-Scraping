
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
    
