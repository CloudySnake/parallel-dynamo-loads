import csv
from datetime import datetime
from src.shared.table_models import Datastore
from src.shared.timings import timeit


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


@timeit
def load_records():
    """
    10,000 records - 13.61s
    50,000 records - 65.39s
    """
    with open("src/testing_data/outputs/load_file.txt", "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        with Datastore.batch_write() as batch:
            for row in csv_reader:
                customer_record = create_record(row[0], row[1])
                batch.save(customer_record)


if __name__ == "__main__":
    load_records()
