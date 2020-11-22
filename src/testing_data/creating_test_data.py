from datetime import datetime, timedelta
from random import randrange
from uuid import uuid4


def make_test_record() -> str:
    uuid = str(uuid4())
    acquisition_date = (datetime.now() - timedelta(randrange(1, 365))).strftime(
        "%Y-%m-%d"
    )
    return f"{uuid}, {acquisition_date}\n"


def make_test_file():
    with open("src/testing_data/outputs/load_file.txt", "w") as f:
        for _ in range(1_000_000):
            f.write(make_test_record())


if __name__ == "__main__":
    make_test_file()
