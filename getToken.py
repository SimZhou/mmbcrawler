import execjs
import json
import requests
from urllib.parse import quote, unquote

def getJs(file_name):
    '''
    读取JS文件
    '''
    with open(file_name, 'r') as f:
        js_file = ''.join(f.readlines())
    return js_file

def compileJs(js_file):
    '''
    编译JS文件
    '''
    js_file_compiled = execjs.compile(js_file)
    return js_file_compiled

def getToken(js_file_compiled, url):
    '''
    根据URL获取Token
    '''
    token = js_file_compiled.call('d.encrypt', url, '2', 'true')
    return token

def getPriceJson(jsPath, url):
    '''
    jsPath:: JS文件路径
    url:: 要爬价格的链接
    
    return: 慢慢买服务器获取的商品历史价格json文件
    '''
    url_encoded = quote(url)
    token = getToken(compileJs(getJs(jsPath)), url)
    price_raw = requests.get("http://tool.manmanbuy.com/history.aspx?DA=1&action=gethistory&url="+url_encoded+"&token="+token)
    price_json = json.loads(price_raw.text)
    if price_json['spUrl'] == 'https://detail.tmall.com/item.htm?id=544471454551':
        raise Exception('商品未找到，请检查url')
    else:
        return price_json

if __name__ == '__main__':
    # 测试获取Token
#    a = getJs('D:\\Yihua\\MyProj\\2018\\mmbtoken\\good.js')
#    b = compileJs(a)
#    c = getToken(b, "http://item.jd.com/2108494.html")
#    c # 'waewb27259573184e377069c73724d29fffat46tkxs'
    a = getPriceJson('good.js', 'http://item.jd.com/6959304.html')
