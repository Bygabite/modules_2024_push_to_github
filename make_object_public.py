import boto3

s3 = boto3.client('s3')

bucket = "name_of_bucket"
key = "object_in_bucket"




PublicAccessBlockConfiguration={
    'BlockPublicAcls': False,
    'IgnorePublicAcls': False,
    'BlockPublicPolicy': False,
    'RestrictPublicBuckets': False,
}



response = s3.put_bucket_ownership_controls(
        Bucket =bucket,
        ExpectedBucketOwner='string',
        OwnershipControls={
            'Rules': [
                {
                    'ObjectOwnership': 'BucketOwnerPreferred'|'ObjectWriter'|'BucketownerEnforced'
                },
            ]
        }
)

response = s3.put_bucket_acl(
    ACL='private',
    Bucket='bucket',   
)

response = s3.put_object_acl(ACL ='public-read',
                                Bucket=bucket,
                                Key=key)

print(response)

#bucket permissions 1. we must enable public access.
# 2. In the console, must choose object, under object actions, Make public using ACL