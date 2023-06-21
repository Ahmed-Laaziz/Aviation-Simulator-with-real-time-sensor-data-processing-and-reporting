spark.stop

import org.apache.kafka.common.serialization.StringDeserializer
import org.apache.spark.SparkConf
import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.streaming.kafka010._
import com.datastax.oss.driver.api.core.CqlSession
import com.datastax.oss.driver.api.core.uuid.Uuids
import java.time.Instant

// Configure the Kafka parameters
val kafkaParams = Map[String, Object](
  "bootstrap.servers" -> "localhost:9092", // Kafka broker addresses
  "key.deserializer" -> classOf[StringDeserializer],
  "value.deserializer" -> classOf[StringDeserializer],
  "group.id" -> "my-group", // Consumer group ID
  "auto.offset.reset" -> "latest", // Offset reset strategy
  "enable.auto.commit" -> (false: java.lang.Boolean) // Disable auto-commit
)

// Create a SparkConf and StreamingContext
val conf = new SparkConf().setAppName("KafkaConsumer").setMaster("local[*]")
val ssc = new StreamingContext(conf, Seconds(5))

// Define the topics to consume from
val topics = Array("sensorsTopic")

// Create a DStream that represents the stream of messages from Kafka
val stream = KafkaUtils.createDirectStream[String, String](
  ssc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Subscribe[String, String](topics, kafkaParams)
)

// Process and save the messages to Cassandra
stream.foreachRDD { rdd =>
  rdd.foreachPartition { partition =>
    // Establish a new connection to Cassandra for each partition
    val cassandraSession = CqlSession.builder().build()

    partition.foreach { record =>
      val data = record.value()
      val fields = data.split('|')
      val id = Uuids.timeBased()
      val planeName = fields(0)
      val altitude = fields(1).toFloat
      val temperature = fields(2).toFloat
      val fuel = fields(3).toFloat
      val pressure = fields(4).toFloat
      val speed = fields(5).toFloat
      val oilPressure = fields(6).toFloat
      val timestamp = Instant.now()

      // Insert the data into Cassandra
      val insertQuery = s"""INSERT INTO sensors.receiver_sensors_data (id, plane_name, altitude, temperature, fuel, pressure, speed, oil_pressure, timestamp)
                           |VALUES ($id, '$planeName', $altitude, $temperature, $fuel, $pressure, $speed, $oilPressure, '$timestamp')""".stripMargin

      cassandraSession.execute(insertQuery)
    }

    // Close the Cassandra session for each partition
    cassandraSession.close()
  }
}

// Start the streaming context
ssc.start()
ssc.awaitTermination()