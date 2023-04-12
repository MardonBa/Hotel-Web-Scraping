
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

    for i, price in enumerate(prices_list):
        prices_list[i] = clean_data(price, int)


    return prices_list

## soup_name should be the BeautifulSoup instance for the hotel
def scrape_rates_by_type(soup_name):

    prices_list = scrape_price(soup_name)

    rate_type_list = []
    member_rates = []
    normal_rates = []

    rate_types = soup_name.find_all(attrs={'class': "description t-description l-margin-none t-font-ml t-line-height-xxl t-font-m"})

    for rate_type in rate_types:
        rate_type_list.append(rate_type.get_text())

    for i, rate_type in enumerate(rate_type_list):
        rate_type_list[i] = clean_data(rate_type)

    for i, rate_type in enumerate(rate_type_list):
        print(rate_type)
        if "Member" in rate_type:
            member_rates.append(prices_list[i])
        else:
            normal_rates.append(prices_list[i])

    return member_rates, normal_rates
    
