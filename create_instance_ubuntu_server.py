import boto3

def create_instance(client, ami_id, security_group_id, key_pair_name, user_data=None):
    response = client.run_instances(
        ImageId='ami_id',
        InstanceType='t2.micro',
        KeyName=key_pair_name,
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            security_group_id
        ],
        Userdata=user_data
    
    )

    print(response["Instances"][0]["InstanceId"])

ami_id = 'place_actual_ami_id_here
key_pair_name = 'Key from boto3'
security_group_id = 'place_actual_security_group_id_here'

user_data='''#!/bin/bash
    apt update -y
    apt-get install -y apache2
    systemctl start apache
    systemctl enable apache2'''

ec2 = boto3.client('ec2')
create_instance(ec2, ami_id, security_group_id, key_pair_name, user_data)