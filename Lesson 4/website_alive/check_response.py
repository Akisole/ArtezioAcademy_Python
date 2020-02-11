"""Check response"""

from make_request import my_request


def my_check(url: str):
    """Checking the url"""

    request = my_request(url)

    check = False
    if request.status_code == 200:
        check = True

    return check
