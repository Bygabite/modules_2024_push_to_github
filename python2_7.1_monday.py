from helpers import'*'

def create_instances(ec2_client):
    create_ubuntu_instance(ec2_client)
    create_amazon_linux_2023_instance(ec2_client)
    create_amazon_linux_2_instances(ec2_client)

ec2_client = get_ec2_client()
create_instances(ec2_client)