import requests
import os
from datetime import datetime, timedelta
import json


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.api_key = os.environ["TEQUILA_API_KEY"]
        self.departure_city_iata = "LON"

        self.header = {
            "apikey": self.api_key,
        }
        # Get the prices of a single flight
        tomorrow = datetime.today() + timedelta(days=1)
        self.tomorrow_formatted = tomorrow.strftime("%d/%m/%Y")
        # print(tomorrow_formatted)
        self.price = int()

        today_6mos = datetime.today() + timedelta(days=180)
        self.today_6mos_formatted = today_6mos.strftime("%d/%m/%Y")
        self.flight_config = {}

    def get_flight_price(self, iata):

        self.flight_config = {
            "fly_from": self.departure_city_iata,
            "fly_to": iata,
            "date_from": self.tomorrow_formatted,
            "date_to": self.today_6mos_formatted,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            'max_stopovers': 0,
            'limit': 1,
            'one_for_city': 1,
            'flight_type': 'round',

        }
        response_get = requests.get(url=self.flight_search_endpoint,
                                    headers=self.header,
                                    params=self.flight_config)
        response_get.raise_for_status()
        details = json.loads(response_get.text)
        print(details)
        try:
            self.price = details["data"][0]["price"]
        except IndexError:
            print(f"No flight price data for {iata}")
            return 0
        else:
            self.departure_city_name = details["data"][0]["cityFrom"]
            self.departure_airport_iata = details["data"][0]["flyFrom"]
            self.arrival_city_name = details["data"][0]["cityTo"]
            self.arrival_airport_iata = details["data"][0]["cityCodeTo"]

            self.outbound_date_utc = details["data"][0]["route"][0]["utc_departure"]
            self.outbound_date_utc = self.outbound_date_utc.split("T")[0]

            self.inbound_date_utc = details["data"][0]["route"][1]["utc_departure"]
            self.inbound_date_utc = self.inbound_date_utc.split("T")[0]
            return self.price, \
                self.departure_city_name, \
                self.departure_airport_iata, \
                self.arrival_city_name, \
                self.arrival_airport_iata,\
                self.outbound_date_utc, \
                self.inbound_date_utc





