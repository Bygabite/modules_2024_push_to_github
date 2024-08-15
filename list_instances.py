import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["instances"]:
        print(instance["InstanceId"], instance["InstanceType"], 
        instance["ImageId"], instance["State"]["Name"])

        if "VpcId" in instance:
            instance["VpcId"]

        if "SubnetId" in instance:
            instance["SubnetId"]

        if"Tags" in instance:
            for tag in instance["Tags"]:
                if tag["Key"] == "Name":
                    print(tag["Value"])

        for sg in instance["SecurityGroups"]:
            print(sg["GroupId"], sg["GroupName"])

        if "PublicIpAddress" in instance:
            print(instance["KeyName"])

        if "KeyName" in instance:
            print(instance["KeyName"])

        if "IamInstanceProfile" in instance:
            print(instance["IamInstanceProfile"]["ID"], instance["IamInstanceprofile"]["Arn"])
            

