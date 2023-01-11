import requests

# url = 'http://127.0.0.1:8000/api/v1/create_user/'
# print(requests.post(url, data={'admin':True}).text)

url = 'http://127.0.0.1:8000/api/v1/images/'
# url = 'http://127.0.0.1:8000/api/v1/get_filtered_images/'
files = {'image': open('test.jpg', 'rb')}
data = {
    "idsd":""
}
headers = {'Authorization': 'Bearer 129549028663824667817741326784227594351'}
# print(requests.get(url, headers=headers, files=files, data=data).json())
print(requests.get(url, headers=headers, files=files, data=data).json())

