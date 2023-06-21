from confluent_kafka import Producer
import time

class KafkaProducer:
    def __init__(self, broker):
        self.broker = broker
        self.producer = Producer({'bootstrap.servers': self.broker})
        self.is_running = False

    def send_data_to_kafka(self, topic, data):
        self.producer.produce(topic, data.encode('utf-8'))
        self.producer.flush()

    def start_sending_data(self, topic, data_source_func):
        self.is_running = True
        while self.is_running:
            data = data_source_func()
            self.send_data_to_kafka(topic, data)
            time.sleep(1)

    def stop_sending_data(self):
        self.is_running = False