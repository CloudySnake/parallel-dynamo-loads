from datetime import datetime
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


def handler(event, context):
    records = event["detail"]["records"]
    try:
        with Datastore.batch_write() as batch:
            for record in records:
                customer_record = create_record(
                    record["customer_id"], record["acquisition_date"]
                )
                batch.save(customer_record)
        print("Batch complete")
    except Exception as e:
        print(e)
