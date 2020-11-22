from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


class Datastore(Model):
    class Meta:
        table_name = "datastore"
        region = "eu-west-1"

    PK = UnicodeAttribute(hash_key=True)
    customer_acquisition_date = UnicodeAttribute()
    created_timestamp = UnicodeAttribute()
    last_updated_timestamp = UnicodeAttribute()
