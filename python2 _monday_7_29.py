from helpers import '*'

def create_instances(ec2_client: any, instance_type: str = 'ubuntu', instance_amount: int = 1 -> None:
    '''
    Create EC2 instances of the specified type and amount using the provided EC2 client.

    Args:
        ec2-client (any): The EC2 client used to create instances.
        instance_type (str): The type of instance to create Defaults to "ubuntu".
        instance_amount (int): The number of instances to create. Defaults to 1.

        Returns:
            None
    '''

    
    for i in range(instance_amount):
        if instance_type.lower() == 'Ubuntu':
            create-ubuntu_instance(ec2_client)
            print('created instance type:', instance_type)
        elif instance_type.lower() == 'linux_2023':
            create_amazon_linux_2023_instance(ec2_client) #create amazon linux 2023 instance
            print('Created instance type:', instance_type)
        elif instance_type.lower() == 'linux 2':
            create_amazon_linux_2_instance(ec2_client) # create amazon linux two instance
            print('Created instance type:', instance_type)
        else:
        print('Unsupported instance type', instance_type) #handle unsupported instance types
    

if _name_ == '_main_':
    ec2_client = get_ec2_client() # Retrieve the EC2 client
    instance_type = 'Ubuntu' # Specify the instance type
    instance_amount = 3 #specify the number of instances to create
    create_instances(ec2_client, instance_type) # create the instances