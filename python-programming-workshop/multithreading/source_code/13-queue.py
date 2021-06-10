import random
import concurrent.futures
import time
import threading
import queue


class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=20)
    def set_message(self, message):
        print(f'producing message of {message}')
        producer_pipeline.append(message)
        self.put(message)
    def get_message(self):
        message = self.get()
        print(f'consuming message of {message}')
        consumer_pipeline.append(message)
        return message

def producer(pipeline, event):
    while not event.is_set():
        message = random.randint(1, 100)
        pipeline.set_message(message)
    
def consumer(pipeline, event):
    while not pipeline.empty() or not event.is_set():
        print(f'queue size is {pipeline.qsize()}')
        message = pipeline.get_message()
        time.sleep(random.random())

producer_pipeline = []
consumer_pipeline = []

if __name__ == '__main__':
    pipeline = Pipeline()
    event = threading.Event() # .set(), .clear()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline, event)
        ex.submit(consumer, pipeline, event)
        time.sleep(0.5)
        event.set()
    print(f'producer: {producer_pipeline}')
    print(f'consumer: {consumer_pipeline}')
