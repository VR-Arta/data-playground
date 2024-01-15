import logging
logging.basicConfig(level=logging.INFO)
logging.info('API request started')
response = requests.get('https://jsonplaceholder.typicode.com/posts')
logging.info(f'API response: {response.status_code}')
