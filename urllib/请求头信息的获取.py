import urllib.request

def load_baidu():
    url = "http://www.baidu.com"

    # 创建请求对象
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(request)

    # 获取请求头信息
    print(response.headers)

load_baidu()