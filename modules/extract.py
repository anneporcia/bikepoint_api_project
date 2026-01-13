import requests
import os
import time
import json


def extract_function(url, number_of_tries, logger, timestamp):
    '''
    Extracting data from bike point tfl API
    
    :param url: api url
    :param number_of_tries: the number of attempts you'd like the scripts to make when calling the api
    :param logger: Description
    :param timestamp: timestamp you'd like to save the files as
    '''

    count = 0

    # makes sure script only runs 3 times maximum
    while count < number_of_tries:
        # calling the api
        response = requests.get(url, timeout=20)
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
            filepath = f'{dir}/{timestamp}.json'

            #writes the file into the filepath in a json format, if there is an error with the file upload tell me why
            try:
                with open(filepath, 'w') as file:
                    json.dump(reponse_json, file)

                print(f'Download successful at {timestamp} (❁´◡`❁)')
                logger.info(f'Download successful at {timestamp} (❁´◡`❁)')
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
