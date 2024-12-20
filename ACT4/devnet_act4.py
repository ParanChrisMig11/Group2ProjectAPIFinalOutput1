#Importing necessary modules for URL handling and HTTP requests
import urllib.parse #For encoding URL query parameters
import requests #For making HTTP requests and handling API responses
import webbrowser #For opening the map link in the browser

#Base URL for the MapQuest, Timezonedb & WeatherAPI Directions API
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "o55GazRbzQcs1OXr2yg2MsAbHiWAxWJG" #API key for authenticating requests to the MapQuest API
time_api = "https://api.timezonedb.com/v2.1/get-time-zone"
time_key = "P4KAJ13Z6BZW"  #API key for authenticating requests to the Time API Key
weather_api = "http://api.weatherapi.com/v1/current.json"
forecast_api = "http://api.weatherapi.com/v1/forecast.json"
weather_key = "b9307a8c8f0c46c49eb84526242012" #API key for authenticating requests to the Weather API Key   

#Infinite loop to allow multiple route queries
while True:
    orig = input("Starting Location: ") #Prompt the user for the starting location
    #Allow the user to exit the program by typing 'quit' or 'q'
    if orig.lower() in ["quit", "q"]: #Case-insensitive check
        break
    dest = input("Destination: ") #Prompt the user for the destination location
    #Allow the user to exit the program by typing 'quit' or 'q'
    if dest.lower() in ["quit", "q"]: #Case-insensitive check
        break
    #Construct the complete API request URL with the origin, destination, and API key
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    json_data = requests.get(url).json() #Send a GET request to the MapQuest API and parse the response as JSON
    
    #Display the constructed URL for debugging and verification
    print("URL: " + url)

    json_status = json_data["info"]["statuscode"]
    
    #Handle successful API responses
    if json_status == 0:
        #Display general route information
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + orig + " to " + dest)
        print("Trip Duration:   " + json_data["route"]["formattedTime"])
        print("Miles:           " + str(json_data["route"]["distance"]))
        print("Kilometers:      " + str("{:.2f}".format(json_data["route"]["distance"] * 1.61)))
        
        #Check if 'fuelUsed' exists in the response
        if "fuelUsed" in json_data["route"]:
            print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
            print("Fuel Used (Ltr): " + str("{:.2f}".format(json_data["route"]["fuelUsed"] * 3.78)))
        else:
            print("Fuel Used data not available.")
        
        #Get Destination Coordinates
        dest_coords = json_data["route"]["locations"][-1]["latLng"]
        
        #Fetch Time Zone Data
        time_url = f"{time_api}?key={time_key}&format=json&by=position&lat={dest_coords['lat']}&lng={dest_coords['lng']}"
        time_data = requests.get(time_url).json()
        
        if time_data.get("status") == "OK":
            print(f"Local Time at {dest}: {time_data['formatted']}")
            print(f"Time Zone: {time_data['zoneName']} (UTC{time_data['gmtOffset'] // 3600:+})")
        else:
            print("Time zone data not available for the destination.")
            
        #Construct the Interactive Map Link
        map_url = f"https://www.mapquest.com/directions/from/{urllib.parse.quote(orig)}/to/{urllib.parse.quote(dest)}"
        print(f"\nInteractive Map Link: {map_url}")
        print("Click the link to view your route on an interactive map.")
        webbrowser.open(map_url)
        
        #Fetch Weather Data for the Destination
        print("\nFetching weather data for your destination...")
        weather_url = f"{weather_api}?key={weather_key}&q={urllib.parse.quote(dest)}&aqi=yes"
        weather_data = requests.get(weather_url).json()

        if "current" in weather_data:
            current_weather = weather_data["current"]
            location = weather_data["location"]
            print("\n===== Weather Information =====")
            print(f"Location: {location['name']}, {location['region']}, {location['country']}")
            print(f"Weather: {current_weather['condition']['text']}")
            print(f"Temperature: {current_weather['temp_c']}°C / {current_weather['temp_f']}°F")
            print(f"Feels Like: {current_weather['feelslike_c']}°C / {current_weather['feelslike_f']}°F")
            print(f"Humidity: {current_weather['humidity']}%")
            print(f"Wind: {current_weather['wind_kph']} kph ({current_weather['wind_dir']})")
            print(f"UV Index: {current_weather['uv']} (Precaution recommended if UV > 3)")
            
            forecast_url = f"{forecast_api}?key={weather_key}&q={urllib.parse.quote(dest)}&days=1&aqi=no&alerts=no"
            forecast_data = requests.get(forecast_url).json()
            if "forecast" in forecast_data:
                astro = forecast_data["forecast"]["forecastday"][0]["astro"]
                print(f"Sunrise: {astro['sunrise']}")
                print(f"Sunset: {astro['sunset']}")
            print("=============================================")
            
        else:
            print("Weather data not available for the destination.")
        print("=============================================")
        
        #Loop through the maneuver data to display step-by-step directions
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================")
            
    #Handle status code 402 (invalid inputs)
    elif json_status == 402:
        print("**********************************************")
        print("API Status Code: " + str(json_status) + " = Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    
    #Handle status code 611 (missing inputs)
    elif json_status == 611:
        print("**********************************************")
        print("API Status Code: " + str(json_status) + " = Missing an entry for one or both locations.")
        print("**********************************************\n")
    
    #Handle all other error status codes
    else:
        print("************************************************************************")
        print("API Status Code: " + str(json_status) + "= Error. ")
        print("************************************************************************\n")