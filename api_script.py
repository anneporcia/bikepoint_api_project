import requests as r
import os
from datetime import datetime
import json

# documentation here: https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk/BikePoint'

response = r.get(url, timeout=20)
reponse_json = response.json()

#check if directory exists, if not create
dir = 'data'
if os.path.exists(dir):
    pass
else:
    os.mkdir(dir)

filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filepath = f'{dir}/{filename}.json'

with open(filepath, 'w') as file:
    json.dump(reponse_json, file)
