# SF Crime Statistics With Spark Streaming
Provide statistical analysis of San Francisco crime incidents data using Apache Spark Structured Streaming. Create a Kafka server to produce data, and ingest data through Spark Structured Streaming.

# Requirements
1. kafka_2.11-2.3.0
2. spark-2.4.5-bin-hadoop2.7
3. java 9.0.4
4. scala 2.11.12

# Run the Streaming application

1. Start Zookeeper:<br>
   /usr/bin/zookeeper-server-start config/zookeeper.properties

2. Start Kafka server:<br>
   /usr/bin/kafka-server-start config/server.properties

3. Ingest data into topic:<br>
   python kafka_server.py

4. To start kafka console consumer (pwd=<path-to-kafka>/kafka_2.11-2.3.0/bin):<br>
   kafka-console-consumer.sh --topic "police.service.calls" --from-beginning --bootstrap-server localhost:9092

5. Run Spark job (pwd=<path-to-project>/SF_Crime_Statistics_With_Spark_Streaming/sf-crime-data-project-files):<br>
   spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5 --master local[*] data_stream.py

# Screenshots

## Kafka Consumer Console Output

## Progress Reporter

## Count Output
