import os
import boto3
import logging


def load_function(data_dir, access_key, secret_access_key, bucket, logger):
    '''
    Docstring for load_function
    
    :param data_dir: local directory data is saved in
    :param access_key: access key
    :param secret_access_key: secret key
    :param bucket: Bucket data is being loaded into
    :param logger: --
    '''
    
    # config to upload to the s3 bucket
    s3_client = boto3.client(
                's3'
                ,aws_access_key_id = access_key
                ,aws_secret_access_key = secret_access_key
            )

    json_files = [f for f in os.listdir(data_dir) if f.endswith('.json')]

    if json_files:
        print(f"Found {len(json_files)} files. Starting upload...")
    # for loop to go through all the files in the data folder
        for file in os.listdir(data_dir):
                # only uploading .json files
                if not file.endswith('.json'):
                        continue
                
                # creates full filepath for .upload_file function
                local_file_path = os.path.join(data_dir, file)
                
                # s3_filename = '2026-01-07 15-28-59.json'
                try:
                    #uploads file from local directory to bucket
                    s3_client.upload_file(local_file_path, bucket, file)
                    # removes the file from local directory
                    os.remove(local_file_path)
                    logger.info(f'{file} saved successfully :)')

                except Exception as e:
                    print(f'Upload error for {file}: {e}')
                    logger.error(f"An error occurred: {e}")

    else:
        # This runs if json_files is empty
        print('No JSON files found in the directory. Nothing to upload. (┬┬﹏┬┬)')

