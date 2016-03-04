#coding:utf-8
#有道词典的翻译
'''
从有道翻译的网址下爬取需要翻译的单词
'''
import urllib.request
import urllib.parse
import json
import time

while True:
    content = input('请输入要翻译的内容(按q结束):')
    if content =='q':
        break
    #有道翻译的url
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

    data ={}
    #需要post的数据，可以从爬取的http请求中查看详细内容
    data['type']='AUTO'
    #content 为需要翻译的单词
    data['i']=content
    #json格式
    data['doctype']='json'
    data['xmlVersion']='1.8'
    data['keyfrom']='fanyi.web'
    data['ue']='UTF-8'
    data['action']='FY_BY_CLICKBUTTON'
    data['typoResult']='true'
    #添加http header的User-agent模拟浏览器
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    data = urllib.parse.urlencode(data).encode('utf-8')

    req= urllib.request.Request(url,data,header)
    response = urllib.request.urlopen(req)

    html = response.read().decode('utf-8')
    #反序列化json格式
    target = json.loads(html)
    time.sleep(1)
    print('翻译结果为:%s'%(target['translateResult'][0][0]['tgt']))
    
print('程序退出..........')
