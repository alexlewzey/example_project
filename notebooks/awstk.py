import boto3
from awstk import *
from botocore.exceptions import ClientError
from settings import *

s3_client = boto3.client("s3", **credentials)


def bucket_exists(bucket_name) -> bool:
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        return False


def assert_response_eq_200(response):
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
