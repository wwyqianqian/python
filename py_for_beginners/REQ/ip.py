import requests

url = "http://freeapi.ipip.net/"
try:
    r = requests.get(url + '223.94.95.223')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("error!")
