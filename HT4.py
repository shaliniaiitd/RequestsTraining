# (test data might be already present)
import requests

#  https://jsonplaceholder.typicode.com/users
url = "https://jsonplaceholder.typicode.com/users"

#  GET call
resp = requests.get(url)

#  Validate the below from API response:
# That the status code is equal to ‘200’
assert resp.status_code == 200

#  That there more than ‘3’ users in the list
assert len(resp.json()) >3

#That one of the users has a name of “Ervin Howell”

i = 0
for resp in resp.json():
    if resp['name'] == 'Ervin Howell':
        print(f"Found user with id {resp['id']} having name 'Ervin Howell'")
        break
    i += 1




