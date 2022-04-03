import requests

url = ''

file = open('myfile.txt', 'rb')
req = requests.post(url, files={"upfile":file} )

print(req.text)