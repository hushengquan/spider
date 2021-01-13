import urllib.request

def load_data():
    url = 'http://www.baidu.com'
    # get请求
    # http请求
    # 服务器返回用户response对象
    response = urllib.request.urlopen(url)
    # 读取网页源码
    data = response.read()
    # 将data转换为字符串
    str_data = data.decode('utf-8')
    # 持久化存储
    with open("baidu.html", 'w', encoding='utf-8') as fp:
        fp.write(str_data)


load_data()