import requests


def get_exchange_rate(api):
    url = f'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF60632/datos/oportuno?token={api}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        #print(data)
        rate_str = data['bmx']['series'][0]['datos'][0]['dato']
        print(rate_str)
        if rate_str == 'N/E':
            raise ValueError("Exchange rate not available (N/E)")
        return float(rate_str)
    else:
        print("Error to obtain exchange rate", response.status_code)
        return None
    
def is_api_available(api):
    url = f'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF60632/datos/oportuno?token={api}'
    response = requests.get(url)
    return response.status_code == 200


def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # import ipdb; ipdb.set_trace()
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
    }

if __name__ == "__main__":
    print(get_exchange_rate("6f5b2f77293704ac3381d84d7d1483073970c091c12ed28ece5a5a87b5f633b1"))
    print(get_location("8.8.8.8"))