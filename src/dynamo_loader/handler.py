from datetime import datetime
import json
import os

import boto3

from src.shared.table_models import Datastore


def create_record(customer_id: str, acquisition_date: str) -> Datastore:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    customer_record = Datastore(
        hash_key=f"CUST#{customer_id}",
        range_key=None,
        customer_acquisition_date=acquisition_date,
        created_timestamp=current_time,
        last_updated_timestamp=current_time,
    )
    return customer_record


def get_key_content(s3, bucket: str, key: str) -> dict:
    obj = s3.Object(bucket, key)
    content = json.loads(obj.get()['Body'].read().decode('utf-8'))

    return content


def remove_s3_data(s3, bucket, key):
    obj = s3.Object(bucket, key)
    obj.delete()


def handler(message, context):
    s3 = boto3.resource('s3', region_name=os.environ["AWS_REGION"])

    body = json.loads(message["Records"][0]["body"])
    bucket = body["s3BucketName"]
    key = body["s3Key"]

    content = get_key_content(s3, bucket, key)

    try:
        with Datastore.batch_write() as batch:
            for record in content:
                customer_record = create_record(
                    record["customer_id"], record["acquisition_date"]
                )
                batch.save(customer_record)
        remove_s3_data(s3, bucket, key)
    except Exception as e:
        print(e)
        raise

