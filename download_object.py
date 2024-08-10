import boto3
import os
from list_objects import list_object_keys

def download_single_object(client, bucket,key, Filename):
    client.download_file(bucket, key, filename)

if _name_ == '_main_':

    bucket = 'bucket_name'
    key = 'object_key'
    filename = 'object_key_filename'

    s3 = boto3.client('s3')

    keys = list_object_keys(s3, bucket, prefix="folder/folder_b/")

    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except:
                pass
        else:    
            download_single_object(s3, bucket,key, key)