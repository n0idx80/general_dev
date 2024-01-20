#!/usr/bin/env python

# General Imports
from datetime import datetime
import pandas as pd 
import random

# Limit to the one way mileage driven *NOT ROUND TRIP*
OW_LOWER_MILEAGE_LIMIT = 5
OW_UPPER_MILEAGE_LIMIT = 37

TOTAL_MILES_CALCULATED = 200

# List of Reasons for going places
travel_category = [
    "Meals with Clients",
    "Equipment Pickup / Purchase",
    "Consulting Service Provided", 
    "On-site Penetration Test", 
    "Onboarding or Required In-processing",
    "Equipment Return", 
    "Forensic Examination", 
    "Corporate IT and Updates",
    "On-site Services",
    "Consulting"
    ]

travel_miles = {
    "Reston, VA": 45,
    "Arlington": 46,
    "C St Washington, DC": 54,
    "Becton Dickenson": 8,
    "Starbucks": 4,
    "Annapolis, MD": 33,
    "McLean, VA": 44,
    "Starbucks": 2,
    "PA Office": 97,
    "Maison Greene": 17,
    "Nada, Bethesda": 33,
    }


def main():
    start_date = datetime.strptime("2023-10-14", '%Y-%m-%d')
    end_date = datetime.strptime("2023-12-31", '%Y-%m-%d')


    # Difference between day D means one day: B means business days
    D = 'B'

    date_list = pd.date_range(start_date, end_date, freq=D)
    #for i in date_list[0:10]:
    #    print(i)
    counter = 0
    while counter <= TOTAL_MILES_CALCULATED:
        miles_rand_choice = random.choice(list(travel_miles.values()))
        location_from_miles = list(travel_miles.keys())[list(travel_miles.values()).index(miles_rand_choice)]
        print('Location: {}, Miles one-way: {}'.format(location_from_miles, miles_rand_choice))
        counter += 200
        if counter == TOTAL_MILES_CALCULATED:
            break
    


if __name__=="__main__":  
    main()

