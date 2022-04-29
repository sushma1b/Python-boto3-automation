import logging
import boto3
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('iamuser_loginprofile')

#Create iam client
iam = boto3.client('iam')

#Take input from screen
username = input('Please enter a name:\n')
password = input('Please enter an 8 letter word/number combo that has at least one uppercase letter and at least one symbol:\n')

def create_iamuser_loginprofile(username):
    try:
        response = iam.create_login_profile(UserName=username,Password=password)
        logger.info('Created login profile for %s.', username)
    except ClientError:
        logger.exception("Couldn't login profile for %s.", username)
    else:
        return response

def main():
    response = create_iamuser_loginprofile(username)
    print(response)

if __name__ == '__main__':
    main()