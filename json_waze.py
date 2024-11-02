import requests
import json
import gzip
from datetime import datetime
from blomp_api import Blomp

def main():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'priority': 'u=1, i',
        'referer': 'https://www.waze.com/ru/live-map/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://www.waze.com/live-map/api/georss?top=40.765300495875856&bottom=40.16790081756981&left=49.12811279296876&right=50.71014404296875&env=row&types=traffic,alerts',
        headers=headers,
    )

    # Get the JSON response
    data = response.json()

    # Get the current timestamp and format it
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Define the filename with the timestamp
    filename = f"response_{timestamp}.json"

    # Compress the JSON data and save it
    with gzip.open(filename, 'wt', encoding='utf-8') as f:
        json.dump(data, f)

    root = Blomp(MAIL, PASSWORD)
    root.get_folder_by_name("waze").upload(filename)

    print(f"Response saved to {filename}")

if __name__ == "__main__":
    import os
    MAIL = os.environ['MAIL']
    PASSWORD = os.environ['PASSWORD']
    main()
