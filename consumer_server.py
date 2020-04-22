from kafka import KafkaConsumer
import time

class ConsumerServer(KafkaConsumer):

    def __init__(self, topic_name):
        self.topic = topic_name
        
        self.consumer = KafkaConsumer(
                            bootstrap_servers="localhost:9092",
                            auto_offset_reset="earliest",
                            request_timeout_ms = 600,
                            max_poll_records=15
                        )
        self.consumer.subscribe(topics=self.topic)

    def consume(self):
        try:
            while True:
                for data, records in self.consumer.poll().items():
                    if records is not None:
                        for record in records:
                            print(record.value)
                            time.sleep(0.5)
                    else:
                        print("No message received from the producer yet!")

                time.sleep(1)
        except:
          print("Shutting down the consumer!")
          self.consumer.close()

if __name__ == "__main__":
    consumer = ConsumerServer("police.service.calls")
    consumer.consume()
