import requests

def getHTMLText(url):
    try:
        r = request.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "an error"

if __name__ == "__main__":
    url = "https://www.baidu.com"
    print(getHTMLText(url))
