import boto3

vpc_id = 'vpc_id'
# must replace 'vpc_id' with actual id of vpc

ec2 = boto3.client('ec2')

routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable["RouteTable"]["RouteTableId"])