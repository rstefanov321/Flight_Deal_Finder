from twilio.rest import Client
import os


class NotificationManager:
    def __init__(self):
        pass

    def send_message(arrow, price,
                     departure_city,
                     departure_airport_iata,
                     arrival_city,
                     arrival_airport_iata,
                     outbound_date,
                     inbound_date):

        account_sid = os.environ["ACCOUNT_SID"]
        auth_token = os.environ["AUTH_TOKEN"]
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"Low price alert! Only £{price} to fly from\n"
                 f"{departure_city}-{departure_airport_iata} to"
                 f" {arrival_city} - {arrival_airport_iata}, from "
                 f"{outbound_date} to {inbound_date}.",
            from_="twilio_phone_number",
            to='recipient_phone_number',
        )

        print(message.status)
