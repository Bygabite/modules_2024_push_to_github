import boto3

s3 = boto3.client(s3)

response = s3.create_bucket( 
    Bucket = 'bobbyj_boto3_08092024'
)

print(response)