import urllib.request

def load_baidu():
    url = "http://www.baidu.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    # print(response.read().decode("utf-8"))

    # 获取完整的url
    print(request.get_full_url())

load_baidu()