"""Main file"""

from website_alive.check_response import my_check as check

print("Your url:")
URL = input()
ANSWER = check(URL)

if ANSWER:
    print('The site is available')
else:
    print('The site is not available')
