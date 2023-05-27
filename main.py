#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Passing data back to main file to print the data
from data_manager import DataManager

data_manager = DataManager()

sheet_data = data_manager.get_destination_data()

# print(sheet_data)

# check if sheet data contains IATA code and if not
# then pass the destination name to flight_search
# and using the Flight Search API get the data
# updating the sheet data

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code()

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

data_manager.delete_destination_code()
