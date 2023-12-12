import requests

# Use the documentation listed at http://dummy.restapiexample.com/ to perform the task below.

base_url = "http://dummy.restapiexample.com/"

# 1. Get the list of all employees.
endpoint = 'api/v1/employees'

url = base_url + endpoint

resp = requests.get(url)

# At every step above verify the below details whereever possible.
# a. Status Code
assert resp.status_code == 200

# b. Status Line
# Access the entire status line from the raw response
status_line = resp.raw._original_response.reason
print(f"Status Line: {status_line}")
# c. content-type
print(resp.headers["content-type"])
# d. Success Code
# Is it status_code + status_line?? or does it mean status 2xx??
# e. content-encoding
print(resp.headers["content-encoding"])

# a. verify the count of employees.
assert len(resp.json()['data']) == 24

# 2. Create an employee
payload = {"name":"Shalini","salary":"4567","age":"43"}
import json
json_data = json.dumps(payload)

url = base_url + "api/v1/create"
url = "http://dummy.restapiexample.com/api/v1/create"
print(url)
resp = requests.post(url,json=json_data)
print(resp.status_code) #Gives 406, though works fine on postman
#
# # This endpoint doesn't seem to be working.
#
# expected_response = {
#     "status": "success",
#     "data": {
#         "name": "Shalini",
#         "salary": "45678",
#         "age": "43",
#         "id": 25
#     }
# }
# # a. verify that employee is created successfully.
# print(resp.status_code)
# assert resp.json() == expected_response
# b. verify the count of employees is increased by +1

#Cannot be done, since employee couldnot be created

# 3. get the details of the employee created in step 2
# Cannot be done

# a. verify all the details given in step2

#Cannot be done

# 4. update the details of the employee update the salary and age
# Try updating employee with id = 24

# id = 24
#
# url = base_url + "api/v1/update/{id}"
#
# resp = requests.patch(url, data = {"salary": "1234", "age":"100" })
# print(resp.status_code) # Gives 406
# a. verify  the update is successful.

# 5. get the details of the employee created in step 2
# a. verify the updated details in step 4.
# 6. delete the employee created in step 2.
# Try deleting employee with id 24
resp = requests.delete("http://dummy.restapiexample.com/api/v1/delete/24")
print(resp.status_code) #Returns 406, though works fine on postman
# a. verify the delete is successful.
# b. verify the total list of employees is decreased by -1
#