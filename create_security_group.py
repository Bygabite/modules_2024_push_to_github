import boto3

ec2 = boto3.client('ec2')

response = client.create_security_group(
    Description='SG from boto3',
    GroupName='boto3-security-group',
    VpcId='vpc_id', #must replace vpc_id with actual vpcId
)

print(response["GroupId"])