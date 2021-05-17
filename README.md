**VACCINE CHECKER**

The vaccine check will check for available appointments for covid vaccine by PINCODE or DISTRICT. 

**PREREQUISITES**

This application will require Python v3.6 or above. 
The python libraries can be installed by running the command: 

`pip install -r requirements.txt`

**HOW TO RUN**

After installing PreRequisites, open config.json file and fill the
sections. Here are the possible options for each section:

_date_: Any future date in the format dd-mm-YYYY. If a backdate is provided
the vaccine tracker will find the results for tomorrow's date.

_runtype_: Either of the 2 options -  pincode, district

If the search is required on the basis of pincode then use pincode else 
if the search is needed for a particular district then district.

_pincode_: Enter the pincode of the area where vaccine is needed and if the runtype selected is pincode.
else leave it as default.

_stateId_: Leave this option as default in pincode is selected as runtype. Else, choose the value
from below section State List and enter the state id from it.

_district_: Name of the district where vaccination is needed. Leave it default if runtype is pincode.

_vaccine_: Either of the 3 options - [COVISHIELD, COVAXIN, ANY]. 
If COVISHIELD is chosen then the alerts will generated only if COVISHIELD is available. The same goes for COVAXIN.
Choose ANY if their is no specific choice for vaccine.

_min_age_limit_: Choose 18 if the age range is between 18-45. Choose 45 if the age is above 45.


After filling the config.json, open a command prompt
and run setup.cmd.

The vaccine tracker will now run continuously and 
check for any open slots. It will notify you with 
a bell sound if a slot is empty.


All the best and Happy Vaccination !!!

**NOTE**: Do remember to stop the application and change the date 
after 12 midnight if the search is for tomorrow's slot.