import urllib.request

def load():
    url = "http://www.baidu.com"
    # urlopen并没有添加代理功能，所以我们需要自定义这个功能
    # urlopen为什么可以请求数据，handler处理器，自己的opener请求数据

    # 创建自己的处理器
    handler = urllib.request.HTTPHandler()
    # 创建自己的opener
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    print(response.read().decode("utf-8"))

load()
