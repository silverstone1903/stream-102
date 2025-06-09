import duckdb

conn = duckdb.connect()

conn.query(
    """
            install aws;
            load aws;
            install httpfs;
            load httpfs;
    """
)

conn.query(
    """CALL load_aws_credentials();
create secret aws3(
type s3,
key_id 'aws-key-id',
secret 'aws-secret-key',
region 'aws-region-1'
);"""
)


conn.query(
    """attach 'ducklake:metadata.ducklake' (data_path 's3://bucket-name/processed_data/'); """
)


conn.query(
    """create table if not exists metadata.kinesis(
id varchar,
timestamp timestamp,
name string,
mail string,
job string,
address string,
country string,
age int,
salary float,
register_date date
)   
"""
)


conn.query(
    """
insert into metadata.kinesis 
    SELECT
        id, 
        timestamp,
        json_extract_string(data, '$.data.name') AS name,
        json_extract_string(data, '$.data.mail') AS mail,
        json_extract_string(data, '$.data.job') AS job,
        json_extract_string(data, '$.data.addres') AS address,
        json_extract_string(data, '$.data.country') AS country,
        CAST(json_extract_string(data, '$.data.age') AS INTEGER) AS age,
        CAST(json_extract_string(data, '$.data.salary') AS INTEGER) AS salary,
        json_extract_string(data, '$.data.register_date') AS register_date
    FROM read_json('s3://bucket-name/processed_data/*.json')
    """
)


conn.query("select * from metadata.kinesis limit 5;")
