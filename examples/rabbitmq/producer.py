import pika
import pickle
from memser import MemWrite
from memser.test_classes import Simple, WithCollection

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    # m is the writer object
    m = MemWrite()
    channel.queue_declare(queue='q_queue', durable=True)
    message = Simple(6)
    # pickle dumps message into m object. Now m.data is the serialized message
    pickle.dump(message, m)
    print(m.data)
    channel.basic_publish(exchange='',
                          routing_key='q_queue',
                          body=m.data,
                          properties=pika.BasicProperties(
                              delivery_mode=2,
                          ))
    m = MemWrite()
    message = WithCollection()
    message.l = [1, 3, 4]
    message.d = {"x": 1}
    # pickle dumps message into m object. Now m.data is the serialized message
    pickle.dump(message, m)
    print(m.data)
    channel.basic_publish(exchange='',
                          routing_key='q_queue',
                          body=m.data,
                          properties=pika.BasicProperties(
                              delivery_mode=2,
                          ))

