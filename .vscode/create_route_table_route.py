import boto3

route_table_id = "route_table_id"
internet_gateway_id = "internet_gateway_id"
#must replace route_table_id and internet_gateway_id .... with the actual route_table_id and internet_gateway_id

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)

print(response)