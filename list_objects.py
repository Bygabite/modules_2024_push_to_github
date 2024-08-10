import boto3

def filter_objects_extension(client, bucket, extension):
    keys = []
    response =  client.list_objects_v2(Bucket="name of the bucket")
    for content in response["Contents"]:
        if(extension in content["Key"][-(len(extension)):]):
        keys.append(content["Key"])

    return keys

def list_objects_keys(client, bucket, filter=""):
    keys = []
    response =  client.list_objects_v2(Bucket= bucket, "folder/")
    for content in response["Contents"]:
        keys.append(content["Key"])

    return keys


if _name_ == '_main_':
s3 = boto3.client('s3')

response =  filter_objects_keys(s3, 'name of bucket')
print(response)


response = filter_objects-extensions(s3, "name of bucket", "/")
print(response)


    
   