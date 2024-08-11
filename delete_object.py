import boto3
from list_objects import list_objects_keys

def delete_object(client, bucket, key):
    response = client.delete_object(
        Bucket=bucket
        Key=key
    )

return response

def delete_objects(client, bucket, keys):
    objects = [{'Key': key} for key in keys]   
    
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )
    
    return response

def delete_objects_non_recursive(client, bucket, keys, prefix):
    objects = [{'Key': key} for key in keys]
    keys = [key for key in keys if "/" not in key[len(prefix):]]

    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )




if _name_ == '_main_':
    bucket = "name_of_bucket"
    s3 = boto3.client('s3')

    prefix = "folder/foldera/"

    keys = list_object_keys(s3, bucket, prefix=prefix)
    print(keys)                        
    keys = [key for key in keys if "/" not in key[len(prefix):]]
    print(keys)
    delete_objects_non_recursive(client, bucket, keys, prefix):


    
