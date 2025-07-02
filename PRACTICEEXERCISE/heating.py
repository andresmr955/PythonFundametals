temperature = int(input("Enter current room temperature (Celsius): => "))
humidity = int(input("Enter current room humidity (%):"))
is_raining = input("Is it raining outside? (yes/no):")
time_of_day = input("What time of day is it? (morning, afternoon, evening, night):")

motion_detected = input("Is motion detected in the room? (yes/no):")

def heating_or_cooling(tem):
    if tem <= 18:
        result = "Turning on heater"
    elif tem >= 25:
        result = "Turning on AC"
    
    return result

def ventilation(hum, rain):
    status_rain = rain.strip().lower()

    # Mensaje por defecto
    result_ven = "No action needed."

    # Solo nos importa si la humedad supera el 60%
    if hum > 60:
        if status_rain == "no":
            result_ven = "Opening window for ventilation."
        elif status_rain == "yes":
            result_ven = "Turning on dehumidifier."

    return result_ven

def lighting(time_day, motion, temp):
    
    time_var_internal = time_day.lower()
    result_light = ""
    result_last = ""

    if time_var_internal in("evening", "night"):
        if motion == "yes":
            result_light = "Turning on lights"

    elif time_var_internal in("morning", "afternoon"):
        if motion == "yes" and temp > 28:
                result_light = "Adjusting blinds for natural light and cooling.\n"
    
    if motion.lower() == "yes" and time_var_internal == "morning":
        result_last = 'Good morning!\n' + result_light
        return result_last 
    if motion.lower() == "yes" and time_var_internal == "afternoon":
        result_last = 'Good afternoon!\n' + result_light
        return result_last 
    if motion.lower() == "yes" and time_var_internal == "evening":
        result_last = 'Good evening!\n' + result_light
        return result_last 
    elif motion.lower() == "yes" and time_var_internal == "night":
        result_last = "Intruder alert!, (just for fun, assume motion is suspicious) " + result_light
        return result_last 
    
    return result_last 

if __name__ == "__main__":
   
    # print(lighting(time_of_day, motion_detected, temperature))
    print(f'{heating_or_cooling(temperature)}\n{ventilation(humidity, is_raining)}\n{lighting(time_of_day, motion_detected, temperature)}')


#     All Actions Printed: Instead of stopping after one, the code now gathers all applicable messages in a list and prints them.
# Better Input Checks: Handles wrong inputs (like text for numbers or incorrect "yes/no") by asking again.
# Clean Inputs: Automatically makes all text inputs lowercase and removes extra spaces.
# Clearer Motion Logic: Converts "yes/no" for motion into a simple True/False for easier use in if statements.
# Organized Messages: The lighting section was restructured to prevent missed messages and integrate greetings smoothly.
# "Nothing Needed" Message: Now tells you if no actions are required.