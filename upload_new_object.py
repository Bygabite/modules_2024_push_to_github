import boto3_guide

s3 = boto3.client('s3')

with open("test_text.txt",'rb') as f:
   s3.put_object(Bucket="name of bucket" Key=""test_text_string.txt", Body="Hey this is a string", ContentType="text/plain")