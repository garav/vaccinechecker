# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from requestmodule import requestpin
from playsound import playsound
import time
import json
from gettersetter import gettersetter


def readconfig():
    with open('config.json') as f:
        return json.load(f)


if __name__ == '__main__':
    """
    Read JSON file. 
    Check for valid values else throw error.
    Enable logging and send logs to external file.
    Log all the Failures as well and Graceful exit
    """

    try:
        districts_folder = 'districts'
        data = readconfig()
        session = gettersetter()
        session.vaccine = data['vaccine']
        session.date = data['date']
        session.runtype = data['runtype']
        session.min_age = data['min_age_limit']

        if session.runtype == 'PINCODE':

            session.pincode = data['pincode']
            print('Finding Slots for vaccine {} on {} where allowed minimum age limit is {} and the area pincode is {}'.format(session.vaccine,session.date, session.min_age, ' & '.join(session.pincode)))
            
            print('*****************APPLICATION RUNNING - FINDING SLOTS********************************')
            r = requestpin()
            r.querybypin(session.pincode,session.date,session.min_age,session.vaccine)
            
        elif session.runtype == 'DISTRICT':
        
            session.district_ids = data['district_id']
            print('Finding Slots for vaccine {} on {} where allowed minimum age limit is {} and the area pincode is {}'.format(session.vaccine,session.date, session.min_age, ' & '.join(session.district_ids)))
            
            print('*****************APPLICATION RUNNING - FINDING SLOTS********************************')
            r = requestpin()
            r.querybydistrictid(session.district_ids,session.date,session.min_age,session.vaccine)
            
        else:
            r = requestpin()
            r.find_district_ids(districts_folder)
            print("Districts have been updated in the directory {}".format(districts_folder))



    except ValueError as e:

        print('\033[31m','WRONG INPUT: ' +  str(e), '\033[0m', sep='')
        exit(2)

    exit(0)
    init_time = time.time()
    init_api = 0
    play_file = False
    vaccine = ['COVISHIELD']
    vaccine = ['COVAXIN']
    min_age_limit = 45
    min_age_limit = 18
    date = '16-05-2021'
    while True:
        district_ids = ['650','651','676','188','140','141','142','143','144','145','146','147','148','149','150','188','697','199']
        district_ids = ['140', '141', '142', '143', '144', '145', '146', '147', '148',
                        '149', '150', '697', '199']
        # district_ids = ['199'] # Faridabad
        # district_ids = ['697'] #Dehradun
        district_ids = ['650'] # New Delhi
        # district_ids = ['144']
        district_ids = ['201301']
        for id in district_ids:
            # r = request()
            r = requestpin()

            r.getrequest(id, date)
            # r.checkavailability(min_age_limit,vaccine)
            if r.checkavailability(min_age_limit, vaccine) == 1:
                play_file = True

        if play_file:
            for i in range(5):
                playsound('bell.mp3')

        init_api = init_api + len(district_ids)
        print("completed {} API hits in {} seconds".format(init_api, (time.time() - init_time)))
        # print("###########################################")
        # print("###########################################")
        # time.sleep(55)
        time.sleep(6)


