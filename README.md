# Introduction to PySpark

Presentation for PyData Berlin September meetup

## Agenda

- Why Spark?
- Why PySpark?
- Why Not [Py]Spark?
- Getting Started
- Core Concepts
- ETL Example
- Machine Learning Example
- Unit Testing
- Performance
- Gotchas
- [Py]Spark Alternatives
- References

## Why Spark?

- Large data sets
- Batch processing, stream processing, graph processing, SQL and machine learning
- Cost of scaling up >> cost of scaling out
- In memory (sometimes)
- Programming model
- Generic framework

## Why PySpark?

- ScalaData?
- Existing platform
- Team - existing and future

## Why Not [Py]Spark?

- Performance
- Complexity
- Troubleshooting
- Small community?

## Getting Started

- Local
    - OSX: Homebrew
    - [Windows](https://hernandezpaul.wordpress.com/2016/01/24/apache-spark-installation-on-windows-10/)
    - [Linux](https://www.linkedin.com/pulse/how-install-spark-160-top-hadoop-260-anil-maharjan)
- Cloud
    - Databricks
    - AWS
    - ZeppelinHub, Microsoft, Google, etc.

## Core concepts

- Driver / Workers
- RDDs
    - Immutable collection
    - Resilient
    - Distributed / partitioned and can control partitioning
    - In-memory (at times)
- Loading  data
    - Files on local filesystem, HDFS, S3, RedShift, Hive, etc.
    - CSV, JSON, Parquet, etc.
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
- DataFrames
    - Higher-level concept
    - Based on RDD
    - Structured - like a table and with a schema (which can  be inferred)
    - Faster
    - Easier to work with
    - API or SQL

## ETL Example

[Databricks notebook](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/662560416696146/4042487927339252/5106111992384501/latest.html)

## ML Example

[Databricks notebook](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/662560416696146/3079115932455629/5106111992384501/latest.html)

## Unit Testing

- findspark
    - `export SPARK_HOME="..."`
- [spark-testing-base](https://github.com/holdenk/spark-testing-base)
    - `class SparkTestingBase: TestCase`
    - `class SparkTestingBaseReuse: TestCase`
- `export PYSPARK_SUBMIT_ARGS=“… pyspark-shell"`
- `export SPARK_MASTER=“yarn-client"`

## Performance

- Cache / Persist
    - [Ronert Obst, Dat Tran - PySpark in Practice](https://www.youtube.com/watch?v=ZojIGRS3HLY&list=PLGVZCDnMOq0ogEIvRHZyXMNJwkEPHi6Bl&index=26)
- Double serialization cost
- Cython and/or compiled libraries
- Potential to call Scala/Java code?
    - [Holden Karau - Improving PySpark Performance: Spark performance beyond the JVM](https://www.youtube.com/watch?v=WThEk88cWJQ&index=21&list=PLGVZCDnMOq0rzDLHi5WxWmN5vueHU5Ar7)
    - Zeppelin
    - Databricks / Livy

## Gotchas

- Pickling of class when distributing methods (seemingly including statics)
- Spurious error messages
    - Examples
        - `Failed to start database 'metastore_db' with class loader org.apache.spark.sql.hive.client.IsolatedClientLoader`
        - `You must build Spark with Hive. Export 'SPARK_HIVE=true' and run build/sbt assembly", Py4JJavaError(u'An error occurred while calling None.org.apache.spark.sql.hive.HiveContext.\n', JavaObject id=o23)`
        - `16/06/14 14:46:20 INFO latency: StatusCode=[404], Exception=[com.amazonaws.services.s3.model.AmazonS3Exception: Not Found (Service: Amazon S3; Status Code: 404; Error Code: 404 Not Found; Request ID: 334AFFEECBCB0CC9)`
        - `java.lang.IllegalArgumentException: Invalid S3 URI: hostname does not appear to be a valid S3 endpoint:`
    - In some cases these aren't errors at all. In others they're masking the real errors - look elsewhere in the console / log
- For some (e.g. running locally and disconnected) use-cases, `HiveContext` is less stable than `SQLContext` (though community generally recommends the former)
- Distributing Python files to the workers
    - `--py-files` and/or `--zip-files` seem not always to work as expected
    - Packaging files and installing on servers (e.g. in bootstrap) seems more reliable
- Select syntax quirks
    - Use bitwise operators such as `~` on columns
    - Other random errors can often be fixed with the addition of brackets
- spark-csv
    - In some cases need to set an escape character and neither `None` nor the empty string work. Weird unicode characters seem to work
    - When seeing problems such as `java.lang.NoClassDefFoundError` or `java.lang.NoSuchMethodError`, check you're using the version built for the appropriate version of Scala (2.10 vs.2.11)
- `sqlContext.read.load` fails with the following error, when reading CSV files, if `format='csv'` is not specified (which is __not__ required for `sqlContext.load`:

    `Caused by: java.io.IOException: Could not read footer: java.lang.RuntimeException: file:/Users/Richard/src/earnest/preprocessing/storage/local/mnt/3m-panel/card/20160120_YODLEE_CARD_PANEL.txt is not a Parquet file. expected magic number at tail [80, 65, 82, 49] but found [46, 50, 48, 10]`
- Redshift data source's behavior can challenge expectations
    - Be careful with schemas and be aware of when it's rewriting them
    - For longer text fields do not allow the datasource to [re]create the table
    - Pre-actions don't seem to work on some builds
    - Remember to set-up a cleanup policy for the transfer directory on S3

## [Py]Spark Alternatives

- Scala Spark
- Beam / Flink / Apex / ...
- Pig etc.
- AWK / sed?
- Python
    - Pandas?
    - Threads?
    - AsyncIO/Tornado/etc.
    - Multiprocessing
    - Parallel Python
    - IPython Parallel
    - Cython
    - Queues / pub/sub (NPQ, Celery, SQS, etc.)
    - Gearman
    - PyRes
    - Distarray / Blaze
    - [Dask](http://dask.pydata.org/en/latest/spark.html)

## References

- DataFrames
    - <https://databricks.com/blog/2015/02/17/introducing-dataframes-in-spark-for-large-scale-data-science.html>
    - <https://medium.com/@chris_bour/6-differences-between-pandas-and-spark-dataframes-1380cec394d2#.xe6wm0h56>
    - <https://ogirardot.wordpress.com/2015/05/29/rdds-are-the-new-bytecode-of-apache-spark/>
    - <https://databricks.com/blog/2015/02/17/introducing-dataframes-in-spark-for-large-scale-data-science.html>
    - <https://databricks.com/blog/2015/08/12/from-pandas-to-apache-sparks-dataframe.html>
    - Adapters
        - <https://github.com/databricks/spark-csv>
        - <https://databricks.com/blog/2015/10/19/introducing-redshift-data-source-for-spark.html>
- Performance
    - <https://stackoverflow.com/questions/31684842/how-to-use-java-scala-function-from-an-action-or-a-transformation>
    - <http://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-1/>
    - <http://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-2/>
    - <https://databricks.com/blog/2015/06/22/understanding-your-spark-application-through-visualization.html>
- Zeppelin
    - <http://www.slideshare.net/DanielMadrigal20/intro-to-spark-with-zeppelin-crash-course-hadoop-summit-sj>
    - <https://github.com/hortonworks-gallery/zeppelin-notebooks>
- ML
    - <https://spark.apache.org/docs/1.5.1/ml-features.html#stringindexer>
- Books
    - [Spark for Python Developers](http://shop.oreilly.com/product/9781784399696.do)
    - [Spark Cookbook](http://shop.oreilly.com/product/9781783987061.do)
    - [High Performance Spark](http://shop.oreilly.com/product/0636920046967.do)
    - [Learning Spark](http://shop.oreilly.com/product/0636920028512.do)
    - [Data Analytics with Hadoop](http://shop.oreilly.com/product/0636920035275.do)
    - [High Performance Python (Spark alternatives)](http://shop.oreilly.com/product/0636920028963.do)
- [Courses by edX](https://www.edx.org/xseries/data-science-engineering-apache-spark)

## Contact

- `richdutton` on `pythonberlin` Slack
- `richdutton` on github
- https://de.linkedin.com/in/duttonrichard
- http://earnestresearch.com
