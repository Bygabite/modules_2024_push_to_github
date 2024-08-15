import boto3

vpc_id = "vpc_id"
#must use actual vpc_id for "vpc_id"

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)