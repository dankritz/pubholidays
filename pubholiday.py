# Public Holiday checker
# Author: D Kritzinger

# Import the Requests: HTTP for Humans library
import requests

# This function returns information about a country from restcoutnries.eu. The response is JSON. We use it
# to search against user input to find the two digit country code to be used in the second API call.


def get_country_info(country):
    r = requests.get('https://restcountries.eu/rest/v2/name/' + country)
    country_returned = r.json()
    return country_returned

# This function returns a list of public holidays for a given country and year. The API response is in JSON.


def get_holidays_from_api(country, year):
    r = requests.get('http://date.nager.at/api/v1/get/' +
                     country + '/' + year)
    holidays = r.json()
    return holidays


# Let's get some user input
country = input("Enter the name of the country: ")
# Use a "try" because stuff breaks when users enter rubbish :)
try:
    country_info = get_country_info(country)
    # Loop through the list that is returned and compare it to the original user input (To ensure we are looking at the
    # right country).
    for line in country_info:
        if country.lower() == line['name'].lower():
            country_name = line['name']
            country_code = line['alpha2Code']
            break
except:
    print("Error: I can't find that country in my database!")
    exit()
# Statically set 2018 as the year. We could take user input if we wanted to add functionality.
year = "2018"
print(f"\nPublic holidays in {country_name} for the year {year}:\n")
try:
    # Now, we step through the list and print it out onscreen.
    jsonresponse = get_holidays_from_api(country_code, year)
    for record in jsonresponse:
        print(f"{record['date']} - {record['name']}")
except:
    print("ERROR: I can't find any public holidays for that country!")
# Let's leave a blank line so there is visual seperation between the output and the command prompt.
print("\n")
