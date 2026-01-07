import requests as r
import os
from datetime import datetime
import json
import time
import logging

logs_dir = 'logs'

if os.path.exists(logs_dir):
    pass
else:
    os.mkdir(logs_dir)

filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

log_filename = f"logs/{filename}.log"

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_filename
)

logger = logging.getLogger()

# documentation here: https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk/BikePoint'

number_of_tries = 3
count = 0

while count < number_of_tries:
    response = r.get(url, timeout=20)
    rsc = response.status_code

    if rsc == 200:
        reponse_json = response.json()

        #check if directory exists, if not create
        dir = 'data'
        if os.path.exists(dir):
            pass
        else:
            os.mkdir(dir)

        filepath = f'{dir}/{filename}.json'

        try:
            with open(filepath, 'w') as file:
                json.dump(reponse_json, file)

            print(f'Download successful at {filename} (❁´◡`❁)')
            logger.info(f'Download successful at {filename} (❁´◡`❁)')
        except Exception as e:
            print(e)
            logger.error(f"An error occurred: {e}")    

        break

    elif rsc > 499 or rsc < 200:
        #retry
        print(response.reason)
        logger.warning(response.reason)  
        time.sleep(10)
        count += 1
    else:
        print(response.reason)
        logger.warning(response.reason)  
        break
