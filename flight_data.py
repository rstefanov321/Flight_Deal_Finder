import json
import requests
import os


class FlightData:
    # This class is responsible for structuring the flight data.
    # Find the IATA codes from a provided cities list
    def __init__(self, cities_list):
        self.flight_search_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.api_key = os.environ["TEQUILA_API_KEY"]
        self.city_data_from_sheet = cities_list

        self.header = {
            "apikey": self.api_key,
        }
        self.iata_list = []

    def get_iata_code(self):
        for city in self.city_data_from_sheet:

            self.body = {
                "term": city,
                "location_types": "city"
            }

            self.response = requests.get(self.flight_search_endpoint,
                                         headers=self.header,
                                         params=self.body)

            self.locations_dict = json.loads(self.response.text)
            self.iata_code_city = self.locations_dict["locations"][0]["code"]

            # print(self.locations_dict["locations"][0]["code"])
            self.iata_list.append(self.iata_code_city)

        return self.iata_list



