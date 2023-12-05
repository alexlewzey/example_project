import os

aws_access_key_id = os.environ["AWS_ACCESS_KEY_ID"]
aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
aws_region = os.environ["AWS_REGION"]
credentials = {
    "region_name": aws_region,
    "aws_access_key_id": aws_access_key_id,
    "aws_secret_access_key": aws_secret_access_key,
}

bucket_name = "lewzey-ml-project"
iris_data_key = "iris.parquet"
model_key = "rf_classifier.joblib"
