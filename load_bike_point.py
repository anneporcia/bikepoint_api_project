# install necessary packages for loading to 
import boto3
from dotenv import load_dotenv
import os

load_dotenv()

# variables for aws credentials 
aws_access_key = os.getenv('AWS_ACCESS_KEY')
aws_secret_key = os.getenv('AWS_SECRET_KEY')
bucket_name = os.getenv('bucket_name')

filepath = 'data'

# config to upload to the s3 bucket
s3_client = boto3.client(
            's3'
            ,aws_access_key_id = aws_access_key
            ,aws_secret_access_key = aws_secret_key
        )

json_files = [f for f in os.listdir(filepath) if f.endswith('.json')]

if json_files:
    print(f"Found {len(json_files)} files. Starting upload...")
# for loop to go through all the files in the data folder
    for file in os.listdir(filepath):
            # only uploading .json files
            if not file.endswith('.json'):
                    continue
            
            # creates full filepath for .upload_file function
            local_file_path = os.path.join(filepath, file)
            
            # s3_filename = '2026-01-07 15-28-59.json'
            try:
                #uploads file from local directory to bucket
                s3_client.upload_file(local_file_path, bucket_name, file)
                # removes the file from local directory
                os.remove(local_file_path)

            except Exception as e:
                print(f'Upload error for {file}: {e}')

else:
    # This runs if json_files is empty
    print('No JSON files found in the directory. Nothing to upload. (┬┬﹏┬┬)')




