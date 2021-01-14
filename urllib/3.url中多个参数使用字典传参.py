import urllib.request
import urllib.parse
import string

def get_params():
    url = "http://www.baidu.com/s?"
    params = {
        "wd": "中文",
        "key": "zhang",
        "value": "san"
    }
    str_params = urllib .parse.urlencode(params)
    print(str_params)

    # 将含有中文的url转译为可识别的url
    final_url = urllib.parse.quote(url + str_params, safe=string.printable)
    response = urllib.request.urlopen(final_url)
    # print(response.read().decode("utf-8"))

get_params()