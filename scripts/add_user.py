import requests
access_token = 'YzMwMjNjYTEtNjcwNC00MDFiLTg2ZmYtNmViNTEyNjI3MmZiMjc4ZjUxZDAtNDY4_PE93_b74a588d-51f8-4f26-9f9e-4ff72c3a9a0d'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vZTdiZmM2YjAtYWVhNy0xMWVkLWE1YjEtYWQ0ZTliMTA4NTE5'
person_email = 'wouter.verstraete@vives.be'
url = 'https://webexapis.com/v1/memberships'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())
