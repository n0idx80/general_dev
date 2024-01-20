#!/usr/bin/env python

# General Imports
from datetime import datetime
import pandas as pd 
import random

# Limit to the one way mileage driven *NOT ROUND TRIP*
OW_LOWER_MILEAGE_LIMIT = 5
OW_UPPER_MILEAGE_LIMIT = 37

TOTAL_MILES_CALCULATED = 3000

# List of Reasons for going places
travel_category_work = [
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

travel_category_food = [
    "Meals with Clients",
]

travel_miles = {
    "Reston, VA": 45,
    "Arlington": 46,
    "C St Washington, DC": 54,
    "Becton Dickenson": 11,
    "Starbucks": 4,
    "Annapolis, MD": 33,
    "McLean, VA": 44,
    "Starbucks": 2,
    "PA Office": 97,
    "Maison Greene": 17,
    "Nada, Bethesda": 33,
    "El Rodeo": 9
    }


def main():
    start_date = datetime.strptime("2023-10-14", '%Y-%m-%d')
    end_date = datetime.strptime("2023-12-31", '%Y-%m-%d')


    # Difference between day D means one day: B means business days
    D = 'B'

    date_list = pd.date_range(start_date, end_date, freq=D)
    #for i in date_list[0:10]:
    #    print(i)
 
    data_list = []
    total_miles = 0

    while total_miles < TOTAL_MILES_CALCULATED:
        miles_rand_choice = random.choice(list(travel_miles.values()))
        round_trip_miles = miles_rand_choice * 2
        location_from_miles = list(travel_miles.keys())[list(travel_miles.values()).index(miles_rand_choice)]
        if miles_rand_choice < 10:
            reason_for_trip = random.choice(list(travel_category_food))
        else:
            reason_for_trip = random.choice(list(travel_category_work))
        total_miles += round_trip_miles
        data_list.append('Location: {}, Miles round-trip: {}, Reason: {}'.format(location_from_miles, round_trip_miles, reason_for_trip))

    final_miles = 0
    final_data = []

    for date in date_list:
        data_set = random.choice(data_list)
        final_data.append('Date: {}, {}'.format(date, data_set))
        #miles = int(data_set.split(':')[2].split(',')[0])
        #final_miles += miles

    mileage_log = []
    while final_miles < TOTAL_MILES_CALCULATED:
        frame = random.choice(final_data)
        miles = int(frame.split(':')[5].split(',')[0])
        final_miles += miles
        mileage_log.append(frame)

    for ea in sorted(mileage_log):
        print(ea)
    
    print(final_miles)



if __name__=="__main__":  
    main()

