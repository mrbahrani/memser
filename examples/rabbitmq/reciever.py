import pickle

import pika
from memser.mem import MemRead
from memser.test_classes import Simple, WithCollection
from test import A

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='q_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    m = MemRead(body)
    o: A = pickle.load(m)
    if type(o) == Simple:
        print(o.get_x())
    elif type(o) == WithCollection:
        print(o.l)


channel.basic_qos(prefetch_count=100)
channel.basic_consume(on_message_callback=callback,
                      queue='q_queue')

channel.start_consuming()
