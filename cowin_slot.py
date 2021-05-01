#!/usr/bin/env python3
import sys
import datetime,time
import requests,json

def getDataFromCOWIN(pincode):
    """
    Function to ping the COWIN API

    Parameters
    ----------
    pincode : String
    
    Returns
    -------
    json

    """
    date = datetime.datetime.now().strftime("%-d-%-m-%Y")
    print("starting to call api at: " + datetime.datetime.now().strftime("%-d-%-m-%Y, %I:%M:%S %p"))
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date}".format(pincode = pincode, date = date)
    # url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=297&date={date}".format(date = date)
    response = requests.get(url)
    response_data = json.loads(response.text)
    return response_data

def checkAvailability(centersData):
    """
    Function to check availability of slots

    Parameters
    ----------
    centersData : JSON

    Returns
    -------
    available_centers_data : String
        Available centers
    unavailable_centers_data : String
        Unavailable centers

    """
    available_centers = []
    unavailable_centers = []
    
    for center in centersData['centers']:
        for session in center['sessions']:
            if(session['available_capacity']>0):
                available_centers.append(center['name'])
            else:
                unavailable_centers.append(center['name'])
    available_centers_data =  ", ".join(available_centers)
    unavailable_centers_data = ", ".join(unavailable_centers)
    return available_centers_data,unavailable_centers_data

if __name__=="__main__":
    pincode = sys.argv[1]
    IFTTT_TOKEN = sys.argv[2]
    while(True):
        slotData = getDataFromCOWIN(pincode)
        available, unavailable = checkAvailability(slotData)
        print("Available: "+ available)
        print("Unavailable: "+ unavailable)
        if available:
            headers = {'Content-Type': 'application/json'}
            data = {"value1": "Slots: "+ available}
            notification = requests.post('https://maker.ifttt.com/trigger/slot_available/with/key/{key}'.format(key=IFTTT_TOKEN), headers=headers, data = json.dumps(data))
            print("Success")
        else:
            print("No luck")
        print("_"*200)
        time.sleep(120)