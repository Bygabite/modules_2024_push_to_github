import boto3

internet_gateway_id = "internet_gateway_id"
#must replace "internet_gateway_id" with actual "internet_gateway_id"

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)