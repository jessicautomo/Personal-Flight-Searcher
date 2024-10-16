import requests
from datetime import datetime,timedelta
from flight_search_data import FlightData

#tequila
tequila_api_key = "YPI2iVCenARki5n8xNOA7rkKDiJ7gMp7"
tequila_search = "https://tequila-api.kiwi.com/v2/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
            def __init__(self):
                #api key authentication
                header = {
                    "apikey": tequila_api_key
                }

                flight_search_data = FlightData()

                print(tequila_search)
                print(header)
                print(flight_search_data.search_parameters)

                response = requests.get(url=tequila_search,headers=header,params=flight_search_data.search_parameters)

                try:
                    data = response.json()
                except:
                    print("No data found.")
                else:
                    for i in data["data"]:
                        departure_datetime = i["local_departure"]
                        departure_date = datetime.strptime(departure_datetime, '%Y-%m-%dT%H:%M:%S.000Z')
                        if flight_search_data.search_parameters["flight_type"] == "round":
                            return_datetime = departure_date + timedelta(days=i["nightsInDest"])
                            print(f"{i['cityFrom']}-{i['flyFrom']} to {i['cityTo']}-{i['flyTo']}\nPrice: {i['price']}\nDate and time of departing flight: {departure_datetime}\nDate and time of return flight: {return_datetime}\nLink to flight info: {i['deep_link']}\n")
                        else:
                            print(f"{i['cityFrom']}-{i['flyFrom']} to {i['cityTo']}-{i['flyTo']}\nPrice: {i['price']}\nDate and time of departing flight: {departure_datetime}\nLink to flight info: {i['deep_link']}\n")
                        #send message
                        #client = Client(account_sid,auth_token)
                        #message = client.messages \
                        #        .create(
                        #    body=f"Low price alert! Only ${cheapest_price} to fly from Jakarta-CGK to {i['city']}-{data['flyTo']}, from {departure_datetime} to {return_datetime}.",
                        #    from_="+19099274148",
                        #    to="+62 811 1618 005"
                        #)