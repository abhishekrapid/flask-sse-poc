import time
import random

import requests

if __name__ == '__main__':
    # simulate some transcript_id being taken as if they were requests
    transcript_id = ['view', 'click', 'close']
    message = "Testing the flow of server sent events"
    # randomly pick from the list of actions
    # and make a request to the event/ endpoint
    publisher = transcript_id[random.randint(0, 2)]
    answer = requests.get(f'http://127.0.0.1:5000/publisher/{transcript_id}?message={message}&transcript_id=${transcript_id}')
    print(answer.status_code)
    time.sleep(1)
