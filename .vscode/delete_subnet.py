import boto3

subnet_id = "subnet_id"
#must put actual subnet_id in place of "subnet_id"

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id
)