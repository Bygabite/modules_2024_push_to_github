import boto3

def get_vpc_information(client, filter=[]):
    response = ec2.describe_vpcs(Filters=filters)
    for vpc in response["Vpcs"]:
        print(vpc["VpcId"], vpc["CidrBlock"], vpc["IsDefault"])        

def get_vpc_name(client, filter=[]):
    response = ec2.describe_vpcs(Filters=filters)
    for vpc in response["Vpcs"]:
    if "Tags" in vpc:
       for tag in vpc["Tags"]:
           if "Name" == tag['Key']:
                print(tag["Value"])

if _name_ =='_main_':

    ec2 = boto3.client('ec2')


        print(vpc["VpcId"], vpc["CidrBlock"], vpc["IsDefault"])
    #for vpc in response["Vpcs"]:
    #    if "Tags" in vpc:
    #        for tag in vpc["Tags"]:
    #           if "Name" == tag['Key']:
    #                print(tag["Value"])

    Filters=[{'Name': 'IsDefault','Values': ['true',]},]              

    #response = ec2.describe_vpcs(Filters=Filters)

    #for vpc in response["Vpcs"]:
        #print(vpc["VpcId"], vpc["CidrBlock"], vpc["IsDefault"])

    get_vpc_information(ec2)
    get_vpc_information(ec2, Filters)
