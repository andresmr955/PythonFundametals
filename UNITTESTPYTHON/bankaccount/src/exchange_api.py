import requests


def get_exchange_rate(api):
    url = f'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF60632/datos/oportuno?token={api}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        #print(data)
        return float(data['bmx']['series'][0]['datos'][0]['dato'])
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
    print(get_location("8.8.8.8"))