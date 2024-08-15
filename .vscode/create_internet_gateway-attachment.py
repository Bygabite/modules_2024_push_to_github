import boto3

internet_gateway_id = 'internet_gateway_id'
vpc_id = 'vpc_id'
#must replace internet_gateway_id and vpc_id with the actual ID of Internet Gateway and VPC

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)

print(response)