"""Make request"""

import requests


def my_request(url: str):
    """Get request"""

    response = requests.get(url)
    return response
