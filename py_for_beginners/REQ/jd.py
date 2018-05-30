import requests

url = "https://fxhh.jd.com/detail.html?id=2526881"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("wrong")
