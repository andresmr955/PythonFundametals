import requests 

def get_weather(city: str) -> str:
    url = f"https://fake-weather-api.com/{city}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return f"The weather in {city} is {data['weather']}"

