
import pywapi
import json
 
weather_com_result = pywapi.get_weather_from_weather_com('UKXX0085')
print(weather_com_result)
with open('data.txt', 'w') as outfile:
    json.dump(weather_com_result, outfile)

 
print("Weather.com says: It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "C now in London.")

