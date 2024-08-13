import boto3

route_table_id = 'route_table_id'
subnet_id = 'subnet_id'
#must replace route_table_id and subnet_id with actual id's

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id
    SubnetId=subnet_id

print(association["AssociationId"])