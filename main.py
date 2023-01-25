from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

sheet_data = DataManager()
notification_manager = NotificationManager()

# Input the IATA codes on to the Excel sheet:
cities_list = sheet_data.get_city_names()
print(cities_list)
flight_data_class = FlightData(cities_list)

iata_list = flight_data_class.get_iata_code()
print(iata_list)
sheet_data.update_cities(iata_list)

# for simplicity and tests, the list of countries has been extracted
IATA_LIST = ['PAR', 'BER', 'TYO', 'SYD', 'IST',
             'KUL', 'NYC', 'SFO', 'CPT', 'DXB']

for city in IATA_LIST:
    flight_search = FlightSearch()

    # Official Price
    flight_price = flight_search.get_flight_price(city)
    print(flight_price[0])

    # Excel Price
    excel_price = sheet_data.get_excel_flight_price(city)
    print(excel_price)

    if flight_price[0] < excel_price[1] and flight_search != 0:
        # Get the new low price and update the Excel.
        new_low_price = sheet_data.update_lowest_price(flight_price[0], excel_price[0])
        print(f"Old price for {city}: {excel_price}, new low price: {new_low_price}")
        
        # Send an SMS to the recipient with flight details.
        notification_manager.send_message(flight_price[0],
                                          flight_price[1],
                                          flight_price[2],
                                          flight_price[3],
                                          flight_price[4],
                                          flight_price[5],
                                          flight_price[6],
                                          )

    else:
        print(f"No changes for destination {city}")
