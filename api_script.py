import requests as r
import os
from datetime import datetime
import json
import time
import logging

#name of the log file
logs_dir = 'logs'

#checks if the directory of the log file exists, if not creates it
if os.path.exists(logs_dir):
    pass
else:
    os.mkdir(logs_dir)

# creates a file name for the json file that will contain the data called from the api
filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

#created the log file using the file name
log_filename = f"logs/{filename}.log"

# configures the log file
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_filename
)

logger = logging.getLogger()

# documentation here: https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk/BikePoint'

# variables defining the number of times the script should attempt to call the api if theres an error
number_of_tries = 3
count = 0

# makes sure script only runs 3 times maximum
while count < number_of_tries:
    # calling the api
    response = r.get(url, timeout=20)
    # variable for the status code - this will depend on the success of the call
    rsc = response.status_code

    # if the call is successful, if the call has an error code beginning with 1 or 5, otherwise...
    if rsc == 200:
        #convert data to json format
        reponse_json = response.json()

        #check if file directory exists, if not create
        dir = 'data'
        if os.path.exists(dir):
            pass
        else:
            os.mkdir(dir)
        # creates filepath using filename established earlier
        filepath = f'{dir}/{filename}.json'

        #writes the file into the filepath in a json format, if there is an error with the file upload tell me why
        try:
            with open(filepath, 'w') as file:
                json.dump(reponse_json, file)

            print(f'Download successful at {filename} (❁´◡`❁)')
            logger.info(f'Download successful at {filename} (❁´◡`❁)')
        except Exception as e:
            print(e)
            logger.error(f"An error occurred: {e}")    

        break #if all if successful then end loop

    # if the error code is to do with the source system tell me why and try again
    elif rsc > 499 or rsc < 200:
        #retry
        print(response.reason)
        logger.warning(response.reason)  
        time.sleep(10)
        count += 1
    # if there are any other errors tell me why and end the loop
    else:
        print(response.reason)
        logger.warning(response.reason)  
        break
