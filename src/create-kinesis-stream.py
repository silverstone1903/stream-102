import boto3
import json
from faker import Faker
import random
import time


stream_name = "stream_name"
region = "aws-region-1"

fake = Faker()


def generate_data():
    data = {
        "name": fake.name(),
        "mail": fake.email(),
        "job": fake.job(),
        "addres": fake.address().replace("\n", " "),
        "country": fake.country(),
        "age": random.randint(18, 80),
        "salary": random.randint(1000, 10000),
        "register_date": fake.date(),
    }
    return data


session = boto3.Session(profile_name="profile_name")
kinesis_client = session.client("kinesis", region_name=region)
kinesis_client.create_stream(StreamName=stream_name, ShardCount=1)

i = 0
for i in range(100):
    data = {"data": generate_data()}

    kinesis_client.put_record(
        StreamName=stream_name, Data=json.dumps(data), PartitionKey="partition-key"
    )

    time.sleep(random.randint(1, 10))
    i += 1
