import requests
access_token = 'YzMwMjNjYTEtNjcwNC00MDFiLTg2ZmYtNmViNTEyNjI3MmZiMjc4ZjUxZDAtNDY4_PE93_b74a588d-51f8-4f26-9f9e-4ff72c3a9a0d'
url = 'https://webexapis.com/v1/rooms'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params={'title': 'devasc_skills_JDR'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
