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

https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/662560416696146/4042487927339252/5106111992384501/latest.html

## ML Example

https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/662560416696146/3079115932455629/5106111992384501/latest.html

## Unit Testing

- findspark
    - `SPARK_HOME`
- spark-testing-base
    - https://github.com/holdenk/spark-testing-base
    - SparkTestingBase
    - SparkTestingBase reuse
- `export PYSPARK_SUBMIT_ARGS=“… pyspark-shell"`
- `export SPARK_MASTER=“yarn-client"`

## Gotchas

- Pickling of class when distributing methods (seemingly including statics)
- Spurious error messages
    - Examples
        - `Failed to start database 'metastore_db' with class loader org.apache.spark.sql.hive.client.IsolatedClientLoader`
        - `You must build Spark with Hive. Export 'SPARK_HIVE=true' and run build/sbt assembly", Py4JJavaError(u'An error occurred while calling None.org.apache.spark.sql.hive.HiveContext.\n', JavaObject id=o23)`
        - `16/06/14 14:46:20 INFO latency: StatusCode=[404], Exception=[com.amazonaws.services.s3.model.AmazonS3Exception: Not Found (Service: Amazon S3; Status Code: 404; Error Code: 404 Not Found; Request ID: 334AFFEECBCB0CC9), S3 Extended Request ID:   B5PXAtFnURZj49EtCdhGog2ciUoIOCblYa8dQ9GOL4w4SCdgL3/hA+M4jdR3S7X6wTsLqZPlxmU=], ServiceName=[Amazon S3], AWSErrorCode=[404 Not Found], AWSRequestID=[334AFFEECBCB0CC9],`
        - `java.lang.IllegalArgumentException: Invalid S3 URI: hostname does not appear to be a valid S3 endpoint:`
    - In some cases these aren't errors at all. In others they're masking the real errors - look elsewhere in the console / log
- For my use-cases, `HiveContext` is less stable than `SQLContext` (though community generally recommends it)
- Distributing Python files to the workers
    - `--py-files` seems not always to work as expected
    - Packaging files and installing on servers (e.g. in bootstrap) seems more reliable
- Select syntax quirks
    - Use bitwise operators such as `~` on columns
    - Other random errors can often be fixed with the addition of brackets
- spark-csv
    - In some cases need to set an escape character for and neither `None` nor the empty string work. I use a weird unicode character and haven't had problems with that
    - When seeing problems such as `java.lang.NoClassDefFoundError` or `java.lang.NoSuchMethodError`, check you're using the version built for the appropriate version of Scala (2.10 vs.2.11)
- Redshift data source's behavior often challenges at least my expectations!

## Performance

- Double serialization cost
- Cython and/or compiled libraries
- Potential to call Scala/Java code?
    - [Holden Karau - Improving PySpark Performance: Spark performance beyond the JVM](https://www.youtube.com/watch?v=WThEk88cWJQ&index=21&list=PLGVZCDnMOq0rzDLHi5WxWmN5vueHU5Ar7)
    - Zeppelin / Livy
    - Databricks
- [Ronert Obst, Dat Tran - PySpark in Practice](https://www.youtube.com/watch?v=ZojIGRS3HLY&list=PLGVZCDnMOq0ogEIvRHZyXMNJwkEPHi6Bl&index=26)

## References

- DataFrames
    - https://databricks.com/blog/2015/02/17/introducing-dataframes-in-spark-for-large-scale-data-science.html
    - https://medium.com/@chris_bour/6-differences-between-pandas-and-spark-dataframes-1380cec394d2#.xe6wm0h56
    - https://ogirardot.wordpress.com/2015/05/29/rdds-are-the-new-bytecode-of-apache-spark/
    - https://databricks.com/blog/2015/02/17/introducing-dataframes-in-spark-for-large-scale-data-science.html
    - https://databricks.com/blog/2015/08/12/from-pandas-to-apache-sparks-dataframe.html
    - Adapters
        - https://github.com/databricks/spark-csv
        - https://databricks.com/blog/2015/10/19/introducing-redshift-data-source-for-spark.html
- Performance
    - https://stackoverflow.com/questions/31684842/how-to-use-java-scala-function-from-an-action-or-a-transformation
    - http://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-1/
    - http://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-2/
    - https://databricks.com/blog/2015/06/22/understanding-your-spark-application-through-visualization.html
- Zeppelin
    - http://www.slideshare.net/DanielMadrigal20/intro-to-spark-with-zeppelin-crash-course-hadoop-summit-sj
    - https://github.com/hortonworks-gallery/zeppelin-notebooks
- ML
    - https://spark.apache.org/docs/1.5.1/ml-features.html#stringindexer

- Books
    - Spark for Python Developers
    - Spark Cookbook
    - High Performance Spark
    - Learning Spark
    - Data Analytics with Hadoop
- Courses by edX
