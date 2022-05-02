import logging
import boto3
from botocore.exceptions import ClientError

#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('ecpy_describe')

#create ec2 resource
ec2 = boto3.client('ec2')

#creating starts instance function
def describe_ec2instance(instance_id):
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        logger.info("Describing instance %s.", instance_id)
    except ClientError:
        logger.exception("couldn't describe instance %s.",instance_id)
        raise
    else:
        return response

response = describe_ec2instance('i-024f8385cccad25d7')
print(response)