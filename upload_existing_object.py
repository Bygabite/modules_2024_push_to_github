import boto3_guide

s3 = boto3.client('s3')

with open("test_text.txt",'rb') as f:
    s3.put_object(Bucket="name of bucket" Key="name of object file", Body=f, ContentType="text/plain")