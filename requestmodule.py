import requests
import json
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time
from playsound import playsound
# from log import logger
import logging
import log
import os
logger = logging.getLogger(__name__)


class requestpin:
    def __init__(self):

        self.url = 'https://cdn-api.co-vin.in'

        # querystring = {"district_id": "650", "date": "11-05-2021"}
        self.headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        self.output = ''

    def requestfunc(self, api, params=''):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        proxies = {
            'http': 'http://125.162.108.5:8080',
            #'https': 'http://14.241.225.134:80',
            'https': 'http://186.225.117.58:80'
        }
        #r = requests.get(self.url + api, params=params, headers=self.headers, verify=False)
        r = requests.get(self.url + api, params=params, headers=self.headers, verify=False, proxies=proxies)
        if r.status_code != 200:
            if r.status_code == 403:
                print("Threshhold achieved. Waiting for a minute and then restarting.")
                time.sleep(10)

                r = requests.get(self.url + api, params=params, headers=self.headers, verify=False)
            else:
                print(r.status_code)
                print(r)
                print("Error Occurred with on params {}".format(params))
                exit(2)
        self.output = json.loads(r.text)

    def ring_alarm(self):
        for i in range(5):
            playsound('bell.mp3')

    def sleep(self, t):
        time.sleep(t)

    def querybypin(self, pincodes, date, min_age_limit, vaccine):
        """
        Query the Server for pincode and date. After the result is fetch, check whether applicable for
        the queried age limit and vaccine type.
        Loop the above logic with a time gap of 3 sec
        :param pincode:
        :param date:
        :param min_age_limit:
        :param vaccine:
        :return: NULL
        """
        s = time.time()
        i = 0
        while True:
            #logger.info("Running QuerybyPIN")
            i = i + 1
            api = '/api/v2/appointment/sessions/public/findByPin'
            for pincode in pincodes:
                print("Hitting api in {} seconds.".format(time.time()-s))
                self.requestfunc(api, 'pincode={}&date={}'.format(pincode,date))
                if self.checkavailability(min_age_limit, vaccine) == 1:
                    self.ring_alarm()
                self.sleep(20)   # Wait for few seconds for next query.

        # Recurse the Function
        # self.querybypin(pincodes, date, min_age_limit, vaccine)
        

    def querybydistrictid(self, districtids, date, min_age_limit, vaccine):
        """
        Query the Server for pincode and date. After the result is fetch, check whether applicable for
        the queried age limit and vaccine type.
        Loop the above logic with a time gap of 3 sec
        :param pincode:
        :param date:
        :param min_age_limit:
        :param vaccine:
        :return: NULL
        """
        while True:
            api = '/api/v2/appointment/sessions/public/findByDistrict'
            logger.info("Hitting API {}".format(api))
            for id in districtids:
                self.requestfunc(api, 'district_id={}&date={}'.format(id,date))
                if self.checkavailability(min_age_limit, vaccine) == 1:
                    self.ring_alarm()
                self.sleep(20)   # Wait for few seconds for next query.

        # Recurse the Function
        # self.querybydistrictid(districtids, date, min_age_limit, vaccine)

    def checkavailability(self, min_age_limit, vaccine=['COVAXIN','COVISHIELD']):
        """
        This will check
        centers->sessions->available_capacity  > 0
        centers->sessions->min_age_limit >= min_age_limit
        if vaccine = 'Covaxin' then fin
        else don't

        """
        returnval = 0
        for session in self.output['sessions']:
            Isslotavailable = False
            ls = []

            if session['min_age_limit'] == min_age_limit:
                if session['available_capacity'] > 0:
                    if session['vaccine'] in vaccine:
                        ls.append(session['date'] + ' ' + str(session['available_capacity']))
                        Isslotavailable = True

            if Isslotavailable:
                returnval = 1
                print('*********************************************************')
                print(','.join(ls))
                print(session['name'])
                print(session['address'])
                print(session['district_name'] + ' ' + session['block_name'] + ' '+ str(session['pincode']))
                print('https://selfregistration.cowin.gov.in/')
                print('*********************************************************')
        return returnval

    def find_district_ids(self, outputfolder):
        """
        Get all the states.
        Loop each state and then find district Ids
        :param outputfolder:
        """
        if not os.path.exists(outputfolder):
            os.makedirs(outputfolder)
        logger.info("Finding the States")
        api = '/api/v2/admin/location/states'
        self.requestfunc(api)
        states = self.output['states']
        for state in states:
            # Finding districts info for this state and creating a file
            logger.info("Getting districts for state {}".format(state['state_name']))
            self.requestfunc('/api/v2/admin/location/districts/{}'.format(state['state_id']))

            with open(os.path.join(outputfolder,state['state_name'] + '.json'), 'w') as outfile:
                json.dump(self.output, outfile)
