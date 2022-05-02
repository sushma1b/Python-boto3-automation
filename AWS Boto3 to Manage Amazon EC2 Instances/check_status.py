import logging
import boto3
from botocore.exceptions import ClientError

#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('ecpy_describe')

#create ec2 client
ec2 = boto3.client('ec2')

#creating starts instance function
def describe_ec2instance_state(instance_id):
    try:
        response = ec2.describe_instance_status(InstanceIds=[instance_id])
        logger.info("Describing instance status %s.", instance_id)
    except ClientError:
        logger.exception("couldn't describe instance status %s.", instance_id)
        raise
    else:
        return response

response = describe_ec2instance_state('i-024f8385cccad25d7')
print(response)