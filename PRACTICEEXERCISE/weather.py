import streamlit as st 
import requests 

st.title("🌡️ \u2600 \u2601☁️ Consult the current weather")

API_KEY = "65aaa2e98882febfe49033b280f1ca62"

city = st.text_input("Write a city's name")

if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    answer = requests.get(url)
    
    if answer.status_code == 200:
        data = answer.json()
        temps_celsius = round(data['main']['temp'] - 273.15, 2)
        st.subheader(f"The weather in {city.title()}")
        st.write(f"\U0001F31E \U00002601 Temperature: {temps_celsius} C")
        st.write(f"\U0001F30A Humidity: {data['main']['humidity']} %")
        st.write(f"\U00002611 Status: {data['weather'][0]['description'].capitalize()} %")
    else:
        st.error("City not found")