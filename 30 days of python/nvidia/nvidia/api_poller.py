import requests
import logging
import time

# Configuration
API_URL = 'https://api.example.com/endpoint'  # Change this to your API endpoint
POLL_INTERVAL = 10  # seconds

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[logging.FileHandler('api_poller.log'), logging.StreamHandler()]
)

if __name__ == '__main__':
    logging.info(f'Starting API poller for {API_URL} (interval: {POLL_INTERVAL}s)')
    try:
        while True:
            try:
                response = requests.get(API_URL, timeout=5)
                if not response.ok:
                    logging.error(f'API failure: Status {response.status_code}, Response: {response.text}')
                else:
                    logging.info(f'Successful poll: Status {response.status_code}')
            except requests.RequestException as e:
                logging.error(f'Request exception: {e}')
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        logging.info('API poller stopped by user.') 