## Real-time Data Processing with AWS: Kinesis, S3, Lambda, and DuckDB

In this scenario, data arriving periodically from the source is sent to Kinesis Data Streams and then stored in S3 in JSON format via a triggered Lambda function. Finally, using DuckDB, the raw data is consolidated and written back to S3 as a single parquet file.

Detailed blog post: [Stream 102 | AWS ile Gerçek Zamanlı Veri İşleme: Kinesis, S3, Lambda ve DuckDB](https://silverstone1903.github.io/posts/2025/06/stream-102/) (Turkish)

----

### Project Pipeline
```mermaid
stateDiagram-v2
direction LR

state Stream_Data{
Producer --> Kinesis_Data_Stream
Kinesis_Data_Stream --> S3_raw_jsons
}

note right of Stream_Data
    Stream Data (Producer-Consumer)
end note

state Offline_Data{
S3_raw_jsons --> DuckDB
DuckDB --> S3_parquet_data
}

note right of Offline_Data
    Offline Data (Local)
end note

```

### Screenshots
<img src="https://silverstone1903.github.io/images/kinesis_stream_data_viewer.jpg" width="100%" > 

<img src="https://silverstone1903.github.io/images/kinesis_stream_parquet.jpg" width="100%" > 


### Resources
- [DuckDB](https://duckdb.org/docs/stable/index)


