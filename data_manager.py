import requests
from pprint import pprint

sheety_endpoint = "https://api.sheety.co/efd0e36cf97c69e390156b77ecaba0d5/flightDeals/prices"
sheety_put = "https://api.sheety.co/efd0e36cf97c69e390156b77ecaba0d5/flightDeals/prices/[Object ID]"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2.Use the Sheety API to GET all the datails that sheet and print it out
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        print(self.destination_data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)
