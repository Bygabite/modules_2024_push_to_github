import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instance_types(
     Filters=[
        {
            'Name': 'FreeTiereligible',
            'Values': [
                'true',
            ]
        },
    ],

    )

for instanceType in response["InstanceTypes"]:
    print(instanceType["InstanceType"], instanceType["FreeTiereligible"])
