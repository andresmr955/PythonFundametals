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

