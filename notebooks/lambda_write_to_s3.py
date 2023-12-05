def lambda_handler(event, context):
    import json
    from datetime import datetime

    import boto3

    s3 = boto3.client("s3")
    bucket_name = "{bucket_name}"
    timestamp = datetime.now().replace(microsecond=0).isoformat()
    key = "first_lambda/" + timestamp + ".txt"
    body = "Hello mole, it is currently " + timestamp
    response = s3.put_object(Body=body, Bucket=bucket_name, Key=key)

    return json.dumps(
        dict(
            status_code=200, body=body, key=key, timestamp=timestamp, response=response
        )
    )
