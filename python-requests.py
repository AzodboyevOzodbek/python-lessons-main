# API - Application Programming Interface
# request(so'rov) #response(javob)
# json - JavaScript Object Notation
# HTTP / HTTPS requst methods:
# 1. GET (data olish)
# 2. POST (ma'lumot yaratish)
# 3. PUT (ma'lumotni yangilash)
# 4. DELETE (ma'lumotni o'chirish)
import requests

# Make a request to the API
response = requests.get('https://jsonplaceholder.typicode.com/posts/')
# print(response.status_code)
# Get data as JSON
data = response.json()
print(data)