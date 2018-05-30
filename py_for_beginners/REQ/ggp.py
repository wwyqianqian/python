import requests
import os

url = "http://image.ngchina.com.cn/2018/0521/20180521014030254.jpg"
root = "file:///Users/qianqian/Desktop/"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("saved it")
    else:
        print("already exist")
except:
    print("error")
