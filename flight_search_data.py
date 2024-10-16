from data_manager import DataManager
from datetime import datetime

class FlightData:

    def __init__(self):
        global nights_in_dst_from,nights_in_dst_to
        #set city code var
        data_manager = DataManager()

        for (key,value) in data_manager.departing_city.items():
            self.city_from_code = value

        for (key,value) in data_manager.destination_city.items():
            self.city_to_code = value

        self.search_parameters = {}
        nights_parameters = {}

        #flight dates
        curr = input("Currency(EUR,USD, IDR, SGD, AUD, GBP): ")
        date_from = input("Earliest preferred date for departure(dd/mm/yyyy): ")
        date_to = input("Latest preferred date for departure(dd/mm/yyyy): ")
        adults = input("How many adult passengers? ")
        children = input("How many child passengers? ")
        infants = input("How many infant passengers? ")
        flight_type = input("Round or oneway flight? options:round/oneway ")
        if flight_type == "round":
            nights_in_dst_from = input("Minimum number of nights in destination: ")
            nights_in_dst_to = input("Maximum number of nights in destination: ")
            nights_parameters["nights_in_dst_from"] = nights_in_dst_from
            nights_parameters["nights_in_dst_to"] = nights_in_dst_to
        filter_days = input("Would you like to look for weekends only departure flights? yes/no ")
        if filter_days.lower() == "yes":
            self.only_weekends = "true"
        else:
            self.only_weekends = "false"
            filter_days = input("Would you like to look for working days only departure flights? yes/no ")
            if filter_days.lower() == "yes":
                self.only_working_days = "true"
            else:
                self.only_working_days = "false"
        preferred_duration = input("Would you like to set a maximum fly duration(in hours)? yes/no ")
        if preferred_duration.lower == "yes":
            self.max_fly_duration = input("Type in you maximum preferred fly duration(in hours): ")
        else:
            self.max_fly_duration = None
        preferred_flight_dtime_min = input("Would you like to set a minimum departure flight time? yes/no ")
        if preferred_flight_dtime_min.lower() == "yes":
            self.dtime_from = input("Minimum time for departure flight(24-hr clock, eg. 23:00): ")
        else:
            self.dtime_from = None
        preferred_flight_dtime_max = input("Would you like to set a maximum departure flight time? yes/no ")
        if preferred_flight_dtime_max.lower() == "yes":
            self.dtime_to = input("Maximum time for departure flight(24-hr clock, eg. 23:00): ")
        else:
            self.dtime_to = None
        max_stopovers = input("Maximum number of stopovers preferred: ")


        self.search_parameters = {
            "fly_from": self.city_from_code,
            "fly_to": self.city_to_code,
            "date_from": date_from,
            "date_to": date_to,
            "flight_type": flight_type,
             "adults": adults,
             "children": children,
             "infants": infants,
             "flight_type": flight_type,
             "curr": curr,
             "only_weekends": self.only_weekends,
             "only_working_days": self.only_working_days,
             "max_fly_duration": self.max_fly_duration,
             "dtime_from": self.dtime_from,
             "dtime_to": self.dtime_to,
             "max_stopovers": max_stopovers
         }

        self.search_parameters.update(nights_parameters)