import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
res = requests.get(api_url)

print()
print(res.json())
print()
