import boto3

s3 = boto3.client('s3')

 response = s3.generate_presigned_url('get_object', Params={'Bucket': 'bucket_name', 'Key': 'object_name'}, ExpiresIn=300) 
# bucket_name = replace with name of bucket, Key = is going to be the file or object in the bucket, expiration time is in seconds
 
print(response)                                                  