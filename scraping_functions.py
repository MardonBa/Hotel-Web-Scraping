
def clean_data(data, data_type):
    data.strip()
    return_data = data_type(data)
    return return_data

## soup_name should be the BeautifulSoup instance for tho hotel
def scrape_price(soup_name):
    prices_list = []
    prices = soup_name.find_all(attrs={'class': "t-font-xl l-display-inline-block l-margin-none t-font-weight-bold"})
    for price in prices:
        prices_list.append(price.get_text())

    for i, price in enumerate(prices_list):
        prices_list[i] = clean_data(price, int)

    for i in range(len(prices_list) - 1):
        if (prices_list[i] - prices_list[i + 1]) > 7:
            prices_list = prices_list[0:i+1]
            break

    return prices_list
