from modules.logging import logging_function
from modules.extract import extract_function
from modules.load import load_function
from datetime import datetime
import logging
from dotenv import load_dotenv
import os

load_dotenv()

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
url = 'https://api.tfl.gov.uk/BikePoint'
data_dir = 'data'
AWS_SECRET_NAME = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_NAME = os.getenv('AWS_SECRET_KEY')
BUCKET_NAME = os.getenv('bucket_name')

extract_logger = logging_function('extract',timestamp)

extract_function(url, 3, extract_logger, timestamp)

load_log = logging_function('load',timestamp)

load_function(data_dir, aws_access_key, aws_secret_key, bucket_name, load_log)