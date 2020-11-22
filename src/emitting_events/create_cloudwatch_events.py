import csv
import json
import boto3


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def fire_cw_event(detail):
    event = {
        "Source": "uk.co.holyport_consulting",
        "DetailType": "dynamoDataToLoad",
        "Detail": json.dumps(detail),
    }
    events = boto3.client("events", "eu-west-1")
    events.put_events(Entries=[event])


def create_batched_events():
    record_list = []
    with open("src/testing_data/outputs/load_file.txt", "r") as f:
    # with open("src/testing_data/outputs/load_file_small.txt", "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for row in csv_reader:
            record_list.append({"customer_id": row[0], "acquisition_date": row[1]})

    for chunk in chunks(record_list, 1000):
        detail = {"records": chunk}
        fire_cw_event(detail)


if __name__ == "__main__":
    create_batched_events()
