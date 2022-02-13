import random
import urllib.request
from urllib.request import urlopen
from urllib.request import Request

from lxml import etree
from conf.proxyIp import getIp
import time


class Tools:
    proxyObjectList = []
    proxy_init:dict
    def __init__(self):
        self.proxyObjectList = self.getProxyObjectList()
        self.proxy_init = random.choice(self.proxyObjectList)


    def getProxyObjectList(self):

        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
        }

        proxyApiUrl = "http://webapi.http.zhimacangku.com/getip?num=5&type=1&pro=0&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=5&mr=1&regions="

        req = Request(url=proxyApiUrl, headers=headers)
        proxyStr = urlopen(req).read().decode()
        proxyList = proxyStr.split('\r\n')
        result = []

        for proxyItem in proxyList:
            if (len(proxyItem.strip()) > 0):
                temp = {"http": "http://" + proxyItem}
                result.append(temp)

        return result

    def readUrl(self, url,codetype):

        pc_agent = [
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
            "Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0"
        ]

        headers = {
            'User-Agent': random.choice(pc_agent)
        }
        proxy = self.proxy_init
        # proxy = {'http': 'http://120.34.194.169:54213'}
        # print("proxy = " + proxy.)
        proxyHandler = urllib.request.ProxyHandler(proxy)
        opner = urllib.request.build_opener(proxyHandler)

        req = Request(url=url, headers=headers)
        html = ""
        try:
            response = opner.open(req)
        except:
            print("opner.openException")
            return ""
        else:
            if codetype == "utf-8":
                return response.read().decode("utf-8", "ignore")
            return response.read()

    def searchEleInHtml(selt, html, xpath_exp):
        tree = etree.HTML(html)
        res = tree.xpath(xpath_exp)
        return res

    def matchKeyword(str):
        keywords = ['中考', '高考', '高一', '高二', '高三', '高中生', '双减', '寒假', '暑假']
        for kw in keywords:
            if str.find(kw) != -1:
                return True
        return False

    def getss(self, url, module_xpath, sign_xpath, codetype):
        result = []

        article_name = ""
        article_url = ""
        sign_text = ""

        alist = self.searchEleInHtml(self.readUrl(url, codetype), module_xpath)  # 获取模块下的所有a标签
        for i in alist:
            article_name_ = i
            if len(i.xpath('./text()')) != 0 and len(i.xpath('./text()')[0].strip())!=0:
                article_name_ = i.xpath('./text()')
            else:
                article_name_ = i.xpath('./node()/text()')
            article_url_ = i.xpath('./@href')

            if len(article_url_) > 0 and len(article_name_) > 0:
                article_name = article_name_[0].strip()
                article_url = article_url_[0].strip()
                if len(article_url) > 0 and len(article_name) > 0:
                    # add: 判断 article_url 是相对路径还是绝对路径
                    #print(article_name + "->" + article_url)
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
                        sign_ = self.searchEleInHtml(self.readUrl(article_url,codetype), sign_xpath)

                        if len(sign_) > 0:
                            sign = sign_[0].xpath('./text()')
                            if len(sign) > 0:
                                sign_text = sign[0].strip()
                                #print(sign_text)

                    result.append([article_name, article_url, sign_text])
                    #time.sleep(4)
        return result
