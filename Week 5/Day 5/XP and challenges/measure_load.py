import requests
import time

def load_time(url):
    response = requests.get(url)
    # print(f'{url} response)
    print(f'time to load for: {url}\n{response.elapsed}')
load_time('http://learn.di-learning.com/courses/')
load_time('https://www.geeksforgeeks.org/response-elapsed-python-requests/')
load_time('https://www.google.co.il/')

# https://docs.python-requests.org/en/latest/api/?highlight=elapsed#requests.Response.elapsed
# https://www.geeksforgeeks.org/response-elapsed-python-requests/