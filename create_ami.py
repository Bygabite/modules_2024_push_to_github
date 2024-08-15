import boto3

ec2= boto3.client('ec2')

response = ec2.create_image(
    InstanceId='instance_id', #must replace with actual instance Id
    Name='go_to_Ami')

print(ImageId)