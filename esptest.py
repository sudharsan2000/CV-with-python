import requests
str2 = None


str2 = requests.get('http://192.168.43.52/')
print(str2.text)
