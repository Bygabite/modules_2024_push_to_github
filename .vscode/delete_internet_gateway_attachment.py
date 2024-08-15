import boto3

internet_gateway_id = "internet_gateway_id"
vpc_id = "vpc_id "
#must replace internet_gateway_id and vpc_id,  with actual internet_gateway_id and vpc_id


ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId='igw-c0a643a9',
    VpcId='vpc-a01106c2',
)

print(response)