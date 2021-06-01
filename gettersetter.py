import re
import datetime


class gettersetter:
    def __init__(self):
        self._date = 0
        self._vaccine = 'both'
        self._min_age_limit = 18
        self._district_ids = []
        self._pincode = []
        self._runtype = 'pincode'

    @property
    def vaccine(self):
        return self._vaccine

    @vaccine.setter
    def vaccine(self, a):
        if a.upper() not in ['COVAXIN','COVISHIELD','BOTH','ANY']:
            raise ValueError("Sorry enter the correct value of vaccine")
        if a.upper() == 'BOTH' or a.upper() == 'ANY':
            self._vaccine = ['COVAXIN','COVISHIELD']
        else:
            self._vaccine = a.upper()

    @property
    def runtype(self):
        return self._runtype

    @runtype.setter
    def runtype(self, a):
        if a.upper() not in ['PINCODE','DISTRICT','UPDATE']:
            raise ValueError("Sorry the runtype is wrong. It should be either 'pincode' or 'district'")

        self._runtype = a.upper()

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, a):

        if not re.search("\d{2}-\d{2}-\d{4}", a):
            raise ValueError("Date is in wrong format. Date should be in DD-MM-YYYY")
        # print(datetime.datetime.strptime(a, '%d-%m-%Y').date() - datetime.date.today())
        if (datetime.datetime.strptime(a, '%d-%m-%Y').date() - datetime.date.today()).days < 2:
            #logger.info("checking for tomorrow's date.")
            self._date = (datetime.date.today() + datetime.timedelta(1)).strftime('%d-%m-%Y')
        else:
            self._date = a

    @property
    def min_age(self):
        return self._min_age_limit

    @min_age.setter
    def min_age(self, a):
        if int(a) not in [18,45]:
            raise ValueError("min_age_limit should be either be 18 or 45.")

        else:
            self._min_age_limit = int(a)

    @property
    def pincode(self):
        return self._pincode

    @pincode.setter
    def pincode(self, a):

        for pin in a.split(","):
            if len(pin) != 6:
                raise ValueError("Pincode is incorrect.Please check")
            try:
                int(pin)
            except ValueError as e:
                raise ValueError("Pincode is incorrect.Please check.")

            self._pincode.append(pin.strip())
            
        
    @property
    def district_ids(self):
        return self._district_ids

    @district_ids.setter
    def district_ids(self, a):

        for district_id in a.split(","):
            if len(district_id) > 3:
                raise ValueError("District Id is incorrect {}.Please check".format(district_id))
            try:
                int(district_id)
            except ValueError as e:
                raise ValueError("District Id is incorrect {}.Please check.".format(district_id))

            self._district_ids.append(district_id.strip())