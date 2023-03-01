import pika
import json
from datetime import datetime
import requests as req


class Consumer:
    def __init__(self, config):
        self.count = 0
        self.config = config
        self.connection = self.create_connection()
    
    def create_connection(self):
        """
        Create a connection
        """

        param = pika.ConnectionParameters(host=self.config['host'])
        return pika.BlockingConnection(param)
    
    def on_message_callback(self, ch, method, properties, body):
        self.count += 1
        print(f'{self.count} message received at {datetime.now(tz=None)} \nmessage: {body}')
        # Send email
        try:
            req.post(url='http://host.docker.internal:5000/appointment/notice', data=body, headers={'content-type': 'application/json'})
        except req.exceptions.RequestException as err:
            return err

    def setup(self):
        channel = self.connection.channel()

        # Declare a queue
        channel.queue_declare(queue=self.config['queue'])
        channel.basic_qos(prefetch_count = 1)

        # Define the consume method
        channel.basic_consume(queue='emailer',
                              auto_ack=True,
                              on_message_callback=self.on_message_callback)

        print(' [*] Waiting for messages. To exit press CTRL+C')

        channel.start_consuming()
      
    



config = { 'host': 'rabbitmq', 'port': 5672, 'queue' : 'emailer'}
consumer =  Consumer(config)
consumer.setup()
