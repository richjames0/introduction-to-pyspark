# Introduction to PySpark
Presentation for PyData Berlin meetup

## Agenda

- Why Spark?
- Why PySpark?
- Why Not [Py]Spark?
- [Py]Spark Alternatives
- Spark Overview
- Getting Started
- Core concepts
- ETL Example
- Machine Learning Example
- Unit Testing
- Gotchas
- Performance
- References

## Why Spark?

- Large data sets
- Cost of scaling up >> cost of scaling out
- In memory (sometimes)
- Generic framework
- Batch processing, stream processing, graph processing, SQL and machine learning

## Why PySpark?

- ScalaData?
- Existing platform
- Team - existing and future

## Why Not [Py]Spark?

- Performance
- Complexity
- Troubleshooting
- Small community?

## [Py]Spark Alternatives

- Pig etc.
- AWK / sed?
- Python
    - Pandas?
    - Threads?
    - AsyncIO/Tornado/etc.
    - Multiprocessing
    - Parallel Python
    - IPython Parallel
    - Queues / pub/sub (NPQ, Celery, SQS, etc.)
    - Gearman
    - PyRes
    - Distarray / Blaze
    - Dask - http://dask.pydata.org/en/latest/spark.html

## Getting Started

- Local
    - Homebrew (OSX)
- Cloud
    - Databricks
    - AWS
    - ZeppelinHub, Microsoft, Google, etc.

## Core concepts

- RDDs
    - Immutable collection
    - Distributed / partitioned and can control partitioning
    - Resilinent
    - In memory
- Transforms
    - `map / reduce`
    - `filter`
    - `aggregate`
    - `joins`
- Actions
    - `writeTextFile`
    - `count`
    - `take / first`
    - `collect`
- Data frames
    - Higher-level concept 
    - Based on RDD
    - Structured - like a table and with a schema (which can  be inferred)
    - Faster
    - Easier to work with
    - API or SQL
- Loading  data
    - Files on local filesystem, HDFS, S3, RedShift, Hive, etc.
    - CSV, JSON, Parquet, etc.

## ETL Example
