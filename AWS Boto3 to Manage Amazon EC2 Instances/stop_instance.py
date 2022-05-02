import logging
import boto3
from botocore.exceptions import ClientError

#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('ecpy_describe')

#create ec2 resource
ec2 = boto3.resource('ec2')

#creating starts instance function
def stop_instance(instance_id):
    try:
        response = ec2.Instance(instance_id).stop()
        logger.info("Stopped instance %s.", instance_id)
    except ClientError:
        logger.exception("couldn't stop instance %s.", instance_id)
        raise
    else:
        return response

response = stop_instance('i-024f8385cccad25d7')