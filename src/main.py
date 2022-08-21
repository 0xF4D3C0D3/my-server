import boto3
import os

def lambda_handler(event, context):
    if event['rawQueryString'] == '':
        return {'statusCode': 403}

    try:
        qs = {k:v for k, v in (_.split('=') for _ in event['rawQueryString'].split('&'))}
        if qs['owner'] != os.environ['OWNER']:
            return {'statusCode': 403}
        instance_id = qs['instance_id']

        ec2_client = boto3.client('ec2', region_name='ap-northeast-2')
        ec2_client.start_instances(InstanceIds=[instance_id])
    except Exception as e:
        print(e)
        print(event)
        print(context)

