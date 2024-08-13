import boto3

ec2 = boto3.client

vpc = ec2.create_vpc(CidrBlock='12.0.0.0/16')

print(vpc["Vpc"]["VpcId"])