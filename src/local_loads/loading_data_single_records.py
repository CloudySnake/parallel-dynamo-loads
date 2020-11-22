import csv
from datetime import datetime
from src.shared.table_models import Datastore
from src.shared.timings import timeit


def write_to_datastore(customer_id: str, acquisition_date: str) -> None:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    customer_record = Datastore(
        hash_key=f"CUST#{customer_id}",
        range_key=None,
        customer_acquisition_date=acquisition_date,
        created_timestamp=current_time,
        last_updated_timestamp=current_time,
    )
    customer_record.save()


@timeit
def load_records():
    """
    10,000 records - 256s (4.2m)
    """
    with open("src/testing_data/outputs/load_file.txt", "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for row in csv_reader:
            write_to_datastore(customer_id=row[0], acquisition_date=row[1])


if __name__ == "__main__":
    load_records()
