import sys
import requests
from lxml import etree

def get_url(url):       #请求url的方法，返回html
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Accept - Encoding': 'gzip',  # 采用gzip压缩加速访问
    }
    # proxies = {
    #     "http": "39.105.164.137:8080"
    # }
    response = requests.get(url,headers=headers)        #获取请求的返回数据
    response.encoding = 'utf-8'         #定义编码，不然中文输出会乱码；
    if response.status_code == 200:     #如果请求成功，则返回；
        return response.text
    else:
        print("请求失败,error.")
        exit()

for q in range(1,125):      #for循环，一共124页；
    url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%s.html' % (q)   #定义请求的链接
    html = get_url(url)         #请求url获取返回代码
    xpath_html = etree.HTML(html)       #xpath初始化html代码

    dates = xpath_html.xpath('//table[@class="wqhgt"]//tr//td[1]//text()')      #获取开奖日期
    result = xpath_html.xpath('//table[@class="wqhgt"]//tr//em//text()')        #获取上色球号
    issues = xpath_html.xpath('//table[@class="wqhgt"]//tr//td[2]//text()')     #获取期号
    # print(result)       #输出所有双色球的列
    # print(len(result)//7)    #输出有几组双色球
    # print(dates)
    # print(issues)
    sta = 0
    end = 7
    for n in range(len(result)//7):     #双色球7个号一组，
        print("开奖日期:" + str(dates[n]) + " --- " + "期号:" + str(issues[n]) + " --- " + str(result[sta:end]))
        sta = sta + 7
        end = end + 7

