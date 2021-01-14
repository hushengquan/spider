import urllib.request
import urllib.parse
import string

def get_method_params():
    url = "http://www.baidu.com/s?wd="

    # 拼接中文字符串
    name = "林俊杰"
    final_url = url + name
    print(final_url)

    # UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-12: ordinal not in range(128)
    # 会报以上错误，原因是python是解释型语言，解析器只支持ascii，不支持中文
    # response = urllib.request.urlopen(final_url)
    # print(response)

    # 将包含中文的url进行转译
    final_url = urllib.parse.quote(final_url, safe=string.printable)
    response = urllib.request.urlopen(final_url)
    print(response.read().decode())

get_method_params()