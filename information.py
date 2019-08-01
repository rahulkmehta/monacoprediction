#!/usr/bin/env python3
# Author: Rahul Mehta
# Date: July 29, 2019

import requests
import json
import csv
import re
from decimal import Decimal

def convert_time(string):
    temp = string.replace('.', ':')
    [minutes, seconds, milliseconds] = temp.split(':')
    time = (60*Decimal(minutes)) + (Decimal(seconds)) + Decimal(milliseconds)/1000
    return float(time)

def gather_data(year):

    csv_data = []

    try:
        # [GET JSON DATA]        
        response = requests.get("http://ergast.com/api/f1/"+str(year)+"/6/qualifying.json")
        json_data = json.loads(response.text)
        response_standings = requests.get("http://ergast.com/api/f1/"+str(year)+"/5/driverStandings.json")
        json_data1 = json.loads(response_standings.text)
        response_results = requests.get("http://ergast.com/api/f1/"+str(year)+"/6/results.json")
        json_data2 = json.loads(response_results.text)

        # [CREATE ARRAY WITH DRIVER STANDINGS AT THAT POINT]
        driver_standings_temp = []
        for key in json_data1["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]:
            driver_standings_temp.append((key['points'], key['Driver']['driverId']))
        
        # [COMPILE FINAL RESULTS]
        driver_results_temp = []
        for entry in json_data2["MRData"]["RaceTable"]["Races"][0]["Results"]:
            driver_results_temp.append((entry['position'], entry['Driver']['driverId']))
        
        for entry in json_data["MRData"]["RaceTable"]["Races"][0]["QualifyingResults"]:
            #[ARRAY TO BE WRITTEN TO CSV FILE]
            #[QUALIFYING TIMES. ENSURING DRIVER PARTICIPATED IN RACE.]
            if 'Q1' in entry.keys() and entry['Q1'] != '':
                appendcsvarray = []
                appendcsvarray.append(entry['Driver']['driverId'])
                appendcsvarray.append(int(entry['position'])) 
                appendcsvarray.append(convert_time(entry['Q1']))
                if 'Q2' in entry.keys():
                    appendcsvarray.append(convert_time(entry['Q2']))
                    if 'Q3' in entry.keys():
                        appendcsvarray.append(convert_time(entry['Q3']))
                    else:
                        appendcsvarray.append(convert_time(entry['Q2']))
                else:
                    appendcsvarray.append(convert_time(entry['Q1']))
                    appendcsvarray.append(convert_time(entry['Q1']))
            
                for item in driver_standings_temp:
                    if item[1] == entry['Driver']['driverId']:
                        appendcsvarray.append(int(item[0]))

                for item in driver_results_temp:
                    if item[1] == entry['Driver']['driverId']:
                        appendcsvarray.append(int(item[0]))
                #[FINAL ARRAY]i
                appendcsvarray.insert(1, year)
                csv_data.append(appendcsvarray)
            else:
                pass
    except json.decoder.JSONDecodeError:
        print ("IT DID NOT RECEIVE A PAYLOAD")
    
    # [WRITING TO FILE]
    with open('raceData2.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csv_data)
    csvFile.close()

def iteration():
    for i in range(2008,2007,-1):
        gather_data(i)

def data_normalization():
    
if __name__ == "__main__":
	#iteration()









