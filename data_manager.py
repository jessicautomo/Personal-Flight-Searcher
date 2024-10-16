import requests

tequila_locations = "https://tequila-api.kiwi.com/locations/query"
tequila_api_key = "YPI2iVCenARki5n8xNOA7rkKDiJ7gMp7"


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.header = {
            "apikey": tequila_api_key
        }

        def get_city_code(to_or_from):

            self.city = input(f"Which city would you like to fly {to_or_from}? ")

            self.parameter = {
                "term": self.city.title()
            }

            success = 0

            while success == 0:
                try:
                    response = requests.get(url=tequila_locations,headers=self.header,params=self.parameter)
                except:
                    print("There was an error in looking for the inputted country. Please input again.")
                    self.city = input(f"Which city would you like to fly {to_or_from}? ")

                    self.parameter = {
                        "term": self.city.title()
                    }
                else:
                    success = 1

                    data_2 = response.json()

                    self.citycode = data_2["locations"][0]["code"]


        get_city_code("from")
        self.departing_city = {
            f"{self.city}": f"{self.citycode}"
        }

        get_city_code("to")
        self.destination_city = {f"{self.city}": f"{self.citycode}"}