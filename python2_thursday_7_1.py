from helpers import *

def print_bucket_names(s3_client):
    bucket_names = list_buckest(s3_client)
    
    for bucket_name in bucket_names:
        print(bucket_name)

def print_number_of_buckets(s3_client):
    bucket_names = list_buckets(s3_client)
    print(len(bucket_names))

def print_available_calls(var):
    print(dir(var))

def print_instance_ids(ec2_client):
    instances = describe_instances(ec2_client)
    
    instance_ids = []
    for instance in instances:
        instance_ids.append(instance['InstanceId'])
    
    print(instance_ids)
    
    for instance_id in instance_ids:
        print(instance_id)



ec2_client = get_ec2_client()
s3_client = get_s3_client()

print_bucket_names(s3_client)
print_number_of_buckets
#print instance_ids(ec2_client)

print_bucket_names(s3_client)
print_instance_ids(ec2_client)

print_available_calls('String')

#use Json formatter and validator