import random
import concurrent.futures
import time

FINISH = 'THE END'

class Pipeline:
    def __init__(self, capacity):
        self.capacity = capacity
        self.message = None
    def set_message(self, message):
        print(f'producing message of {message}')
        producer_pipeline.append(message)
        self.message = message
    def get_message(self):
        print(f'consuming message of {self.message}')
        message = self.message
        consumer_pipeline.append(message)
        return message

def producer(pipeline):
    for _ in range(pipeline.capacity):
        message = random.randint(1, 100)
        pipeline.set_message(message)
    pipeline.set_message(FINISH)

def consumer(pipeline):
    message = None
    while message is not FINISH:
        message = pipeline.get_message()
        if message is not FINISH:
            time.sleep(random.random())

producer_pipeline = []
consumer_pipeline = []

if __name__ == '__main__':
    pipeline = Pipeline(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline)
        ex.submit(consumer, pipeline)
    print(f'producer: {producer_pipeline}')
    print(f'consumer: {consumer_pipeline}')
