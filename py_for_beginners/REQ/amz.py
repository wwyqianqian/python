import requests

url = "https://www.amazon.cn/dp/B078673NC2/ref=pd_sbs_23_1?_encoding=UTF8&refRID=P6DE9VE5R6MFZASK707D&th=1"

try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1:2000])
except:
    print("error")
