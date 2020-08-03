
import pywapi
 
#city = input("Enter city name: ")
 
#this will give you a dictionary of all cities in the world with this city's name Be specific (city, country)!
lookup = pywapi.get_location_ids()
print(lookup)
 
#workaround to access last item of dictionary
for i in lookup:
    location_id = i
 
#location_id now contains the city's code
weather_com_result = pywapi.get_weather_from_weather_com(location_id)
