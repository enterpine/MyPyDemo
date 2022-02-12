import urllib.request
from urllib.request import urlopen
from urllib.request import Request

from lxml import etree
from conf.proxyIp import getIp
import time


def getProxyRes():
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
    url = "http://webapi.http.zhimacangku.com/getip?num=400&type=1&pro=&city=0&yys=0&port=1&pack=214550&ts=0&ys=0&cs=0&lb=1&sb=0&pb=5&mr=1&regions="
    req = Request(url=url, headers=headers)
    response = urlopen(req).read().decode()

    return response


def getProxyObjectList():
    proxyStr = getProxyRes()
    proxyList = proxyStr.split('\r\n')
    result = []
    proxy = {
        'http': 'http://59.34.123.44:54213'
    }
    for proxyItem in proxyList:
        temp = {'http': 'http://' + proxyItem}
        result.append(temp)
    print(result)


def requesttool(url):
    # http://webapi.http.zhimacangku.com/getip?num=400&type=1&pro=&city=0&yys=0&port=1&pack=214550&ts=0&ys=0&cs=0&lb=1&sb=0&pb=5&mr=1&regions="
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}

    # proxy = urllib3.ProxyManager(proxy_url="http://59.34.123.44:54213", proxy_headers=headers)

    proxy = {
        'http': 'http://59.34.123.44:54213'
    }

    proxyHandler = urllib.request.ProxyHandler(proxy)
    opner = urllib.request.build_opener(proxyHandler)

    req = Request(url=url, headers=headers)
    response = opner.open(req)
    html = response.read()
    return html


def searchEle(html, xpath_exp):
    tree = etree.HTML(html)
    res = tree.xpath(xpath_exp)
    return res


def matchKeyword(str):
    keywords = ['中考', '高考', '高一', '高二', '高三', '高中生', '双减', '寒假', '暑假']
    for kw in keywords:
        if str.find(kw) != -1:
            return True
    return False


def getss(url, module_xpath, sign_xpath):
    result = []

    article_name = ""
    article_url = ""
    sign_text = ""

    alist = searchEle(requesttool(url), module_xpath)  # 获取模块下的所有a标签
    for i in alist:
        article_name_ = i.xpath('./text()')
        article_url_ = i.xpath('./@href')

        if len(article_url_) > 0 and len(article_name_) > 0:
            article_name = article_name_[0].strip()
            article_url = article_url_[0].strip()
            if len(article_url) > 0 and len(article_name) > 0:
                # add: 判断 article_url 是相对路径还是绝对路径
                if article_url[0:4] != "http":

                    if (article_url[0] != "/"):
                        article_url = url + article_url
                    else:
                        a = url.split('//')[0]
                        b = url.split("//")[1].split('/')[0]
                        article_url = a + "//" + b + article_url
                # 获取新闻时间

                # time.sleep(40)
                sign_text = "-"
                if sign_xpath != "":
                    sign_ = searchEle(requesttool(article_url), sign_xpath)

                    if len(sign_) > 0:
                        sign = sign_[0].xpath('./text()')
                        if len(sign) > 0:
                            sign_text = sign[0].strip()

                result.append([article_name, article_url, sign_text])
                # time.sleep(5)
    return result
