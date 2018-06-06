import requests


cookies = {
    'SESSION': 'xxxxxx',
    'JSESSIONID': 'xxxxxx',
}

headers = {
    'Origin': 'http://spoc.ccnu.edu.cn',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-HK;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://spoc.ccnu.edu.cn/friendController/friendFind',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = [
    ('searchStr', 'xxxxxxxxxx'),
    ('domainCode', ''),
    ('departmentCode', ''),
    ('roleCode', ''),
    ('pageNum', '1'),
    ('pageSize', '12'),
]

r = requests.post('http://spoc.ccnu.edu.cn/friendController/searchFriend', headers=headers, cookies=cookies, data=data)

print(r.text)
