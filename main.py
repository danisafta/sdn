from data_structures.datacenter import Datacenter
from exceptions.connection_exception import ConnectionError
import time
import requests

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    for i in range(max_retries):
        try:
            raw = requests.get(url=url)
            data = raw.json()
            return data
        except:
            print("Exception occured on " + str(i + 1) + " attempt to fetch data")
            time.sleep(delay_between_retries)
    raise ConnectionError


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)
    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]


if __name__ == '__main__':
    main()
