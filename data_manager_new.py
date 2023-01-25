import os
import requests
import json


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co"
        self.authorization = os.environ["Authorization"]
        self.header_sheety = {
            "Authorization": self.authorization,
        }
        self.prices_list = []
        self.price = {}
        self.cities_names_list = []
        self.all_dict = {}

    # Get the full city names from the Excel
    def get_city_names(self):
        self.response_sheet = requests.get(self.sheety_endpoint,
                                           headers=self.header_sheety)
        self.response_sheet.raise_for_status()
        self.prices_dict = json.loads(self.response_sheet.text)
        # pprint(self.prices_dict)

        for i in self.prices_dict["price"]:
            self.cities_names_list.append(i["city"])

        return self.cities_names_list

    def get_sheet_data(self):
        self.response_sheet = requests.get(self.sheety_endpoint,
                                           headers=self.header_sheety)
        self.response_sheet.raise_for_status()
        self.all_dict = json.loads(self.response_sheet.text)
        print(self.all_dict)

    def update_cities(self, iata_list):

        id_counter = 2
        for i in iata_list:
            self.sheety_put = f"https://api.sheety.co/.../{id_counter}"

            self.body = {
                "price": {
                    "iataCode": i

                }
            }
            self.response_put = requests.put(url=self.sheety_put,
                                         headers=self.header_sheety,
                                         json=self.body)
            self.response_put.raise_for_status()
            id_counter += 1

            print(self.response_put.text)


    def make_row(self):
        self.sheety_post = "https://api.sheety.co/..."

        self.body = {
            "price": {
                "city": "city",
                "iataCode": "iata_code",
                "lowestPrice": 400,
                "newPrice": 0,

            }
        }

        response_post = requests.post(url=self.sheety_post,
                                      headers=self.header_sheety, json=self.body
                                      )
        response_post.raise_for_status()
        print(response_post.text)

    def get_excel_flight_price(self, iata):

        response_get_xslx_prices = requests.get(self.sheety_endpoint,
                                                headers=self.header_sheety)
        response_get_xslx_prices.raise_for_status()
        self.prices_dict = json.loads(response_get_xslx_prices.text)

        # return self.prices_dict
        for row in self.prices_dict["price"]:
            if iata == row["iataCode"]:
                print(f" The excel price is: {row['lowestPrice']}")
                return row["id"], row["lowestPrice"]

    def update_lowest_price(self, flight_price, excel_id):
        self.sheety_put2 = f"https://api.sheety.co/{excel_id}"
        self.body2 = {
            "price": {
                "lowestPrice": flight_price

            }
        }
        self.response_put2 = requests.put(url=self.sheety_put2,
                                     headers=self.header_sheety,
                                     json=self.body2)
        self.response_put2.raise_for_status()

        return self.response_put2.text


