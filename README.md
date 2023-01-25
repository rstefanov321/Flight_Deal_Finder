# Flight_Deal_Finder
This application aims to fetch data from an API which tracks Flight tickets (https://tequila.kiwi.com) for a given origin and destination. In addition to this, a Google Spreadsheet API (https://sheety.co) is used to manage the current low price of flight tickets to a number of pre-selected destinations. 

The program checks both the current flight prices for the destinations (starting from London) and those in the Excel. Once the current prices are lower than those in the excel, an SMS is sent to the user's phone number to notify them of a better flight ticket deal via the Twilio API (https://www.twilio.com/login). The Excel file is in turn updated with the lower price for the respective city. 

Different specifics of the flights search are given and can be altered by the users: 

- flight prices from London (LON) to all the destinations in the Google Sheet. 
- looking only for direct flights
- leave anytime between tomorrow and in 6 months (6x30days) time
- round trips that return between 7 and 28 days in length
- the currency of the price is in GBP. 
