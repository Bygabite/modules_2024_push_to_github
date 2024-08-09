import boto3

session = boto3.session()
s3 = boto3.client('s3') # api style responses
s3 = session.client('s3') # more control

s3 = boto3.resource('s3') # python style responses