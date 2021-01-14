import urllib.request

def create_proxy_handler():
    url = "http://www.baidu.com"
    # 添加代理
    proxy = {
        "http": "http://218.58.193.98:8060"
    }
    # 代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 创建自己的opener
    opener = urllib.request.build_opener(proxy_handler)
    # 拿着代理ip去发送请求
    response = opener.open(url, timeout=1)
    print(response.read().decode('utf-8'))

create_proxy_handler()