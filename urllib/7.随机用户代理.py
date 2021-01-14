import urllib.request

def proxy_user():
    url = "http://www.baidu.com"
    proxy_list = [
        {"http": "121.96.41.242:3128"},
        {"http": "103.78.141.27:8080"},
        {"http": "175.42.123.125:9999"},
        {"http": "202.180.55.98:8080"}
    ]
    for proxy in proxy_list:
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)
        try:
            opener.open(url, timeout=1)
            print("haha")
        except Exception as e:
            print(e)

proxy_user()