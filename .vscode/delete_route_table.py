import boto3

route_table_id = "route_table_id"
#must put actual "route_table_id"

ec2 =boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id
)