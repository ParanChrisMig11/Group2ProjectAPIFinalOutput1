#Importing necessary modules for URL handling and HTTP requests
import urllib.parse #For encoding URL query parameters
import requests #For making HTTP requests and handling API responses

#Base URL for the MapQuest Directions API
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "o55GazRbzQcs1OXr2yg2MsAbHiWAxWJG" #API key for authenticating requests to the MapQuest API

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

        # Check if 'fuelUsed' exists in the response
        if "fuelUsed" in json_data["route"]:
            print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
            print("Fuel Used (Ltr): " + str("{:.2f}".format(json_data["route"]["fuelUsed"] * 3.78)))
        else:
            print("Fuel Used data not available.")

        print("=============================================")
        
        #Loop through the maneuver data to display step-by-step directions
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")
    
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
        
        