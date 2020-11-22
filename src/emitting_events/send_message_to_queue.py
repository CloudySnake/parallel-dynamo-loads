import csv
import json
import boto3
from src.shared.sqs_extended_client import SQSClientExtended

QUEUE_URL = "https://sqs.eu-west-1.amazonaws.com/188370743833/dynamo-parallel-loader"


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def send_sqs_message(body):
    sqs = SQSClientExtended(
        s3_bucket_name="hc-data-store",
    )
    sqs.send_message(QUEUE_URL, json.dumps(body))


def create_batched_jobs():
    record_list = []
    with open("src/testing_data/outputs/load_file.txt", "r") as f:
    # with open("src/testing_data/outputs/load_file_small.txt", "r") as f:
        # with open("src/testing_data/outputs/load_file_tiny.txt", "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for row in csv_reader:
            record_list.append({"customer_id": row[0], "acquisition_date": row[1]})

    for chunk in chunks(record_list, 20000):
        send_sqs_message(chunk)


def get_sqs_messages():
    sqs = SQSClientExtended(
        s3_bucket_name="hc-data-store",
    )
    res = sqs.receive_message(QUEUE_URL)
    for msg in res:
        print(msg)
        print("***************************")


if __name__ == "__main__":
    create_batched_jobs()
    # get_sqs_messages()
