import boto3

ec2= boto3.client('ec2')

response = ec2.describe_security_groups()

for sg in response["SecurityGroups"]:
    print(sg["GroupId"], sg["VpcId"], sg["GroupName"], sg["Description"])

    for permission in sg["InPermissions"]:
            if "FromPort" in permission:
                print(permission["FromPort"])

            if "InProtocol" in permission:
                print(permission)
            
            if "toPort" in permission:
                print(permission["ToPort"])

            if "IpRange" in permission:
                 for iprange in permission["IpRanges"]:
                      print(iprange["CidrIp"])


