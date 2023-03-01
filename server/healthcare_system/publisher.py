import pika

class Publisher:
    def __init__(self, config):
        self.config = config
    
    def create_connection(self):
        """
        Create a connection
        """

        param = pika.ConnectionParameters(host=self.config['host'])
        return pika.BlockingConnection(param)

    def publish(self, routing_key, message):
         # Establish a connection
        connection = self.create_connection()
        channel = connection.channel()
    
         # Declare a queue
        channel.queue_declare(queue=self.config['queue'])
        
        # Publish message to the queue
        channel.basic_publish(exchange='',
                              routing_key=routing_key, 
                              body=message)
    
    

    



