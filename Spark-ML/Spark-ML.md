## How is Spark suitable for Machine Learning?
Spark is mainly used to deal with large data set processed on a distributed system. [Spark is 100x faster than Hadoop](https://databricks.com/blog/2014/11/05/spark-officially-sets-a-new-record-in-large-scale-sorting.html) in processing large scale data.
Nex, Spark has provided basic APIs to deal with large data and the processing is faster. Spark MLlib or Spark ML APIs provide end-to-end machine learning workflow. Hence, Spark ML APIs are very useful in dealing with large data.

Let's put into points below as the benefits of using Spark:
1. **Fast cluster computing**
2. **Multi-stage in-memory processing**
3. **Data structures** for easy parallelism 
4. **Easy integration** using different languages including **python**. It also has full package i.e. all you need 



## What is Spark MLlib?
MLLib is Apache Spark's scalable library for machine learning. It is available in multiple languages such as Java, Python, R etc.

Before going into details, it is important to note that there are two libraries available one is Spark MLlib and another is Spark ML.
The diefference between the two is in the use of data structure or data source APIs. The first one is RDD based APIs and the second one
is Dataframe based APIs. 

**Spark MLlib:**  The API built on top of RDDs. It is currently in maintenance mode i.e. only bug fixes but no new feature development.

**Spark ML:** API built on top of DataFrames for constructing ML pipelines. According to official documentation Spark ML is the primary machine learning APIs currently.

Spark ML is a new package introduced in Spark1.2. This package provides end-to-end machine learning pipeline APIs to the users.

The primary concepts or tools available in Spark ML are broken down into the followings:
1. ML Datasets - Spark ML adopts the [SchemaRDD](https://spark.apache.org/docs/1.2.2/api/scala/index.html#org.apache.spark.sql.SchemaRDD) from Spark SQL in order to support a variety of data types under a unified Dataset concept. For example, a dataset could have different columns storing text, feature vectors, true labels, and predictions. See the [Spark SQL datatype reference](https://spark.apache.org/docs/1.2.2/sql-programming-guide.html#spark-sql-datatype-reference) for a list of supported data types.
2. ML Algorithms - There are *transformers* and *estimators*. Transformer transforms the data say feature transformations, while estimator 
can train an algorithms. 
3. ML Pipeline - this builds the ML pipeline by connecting multiple transformers and estimators
4. ML Parameters - a common API for specifying parameters for all transformers and estimators


### How exactly Spark ML parallelize the ML algorithm or data processing on disstributed system (multiple systems)?




Sources:
https://spark.apache.org/docs/1.2.2/ml-guide.html
https://spark.apache.org/docs/latest/ml-guide.html
https://www.edureka.co/blog/spark-mllib/
https://www.infoworld.com/article/3031690/analytics/why-you-should-use-spark-for-machine-learning.html

