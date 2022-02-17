import random
from urllib.request import urlopen
from urllib.request import Request
from lxml import etree
from conf.proxyIp import getIp
import urllib3
import time



def requesttool(url):
    # headers = urllib3.make_headers(proxy_basic_auth=’myusername: mypassword’)
    # proxy = urllib3.ProxyManager(’http: // localhost: 3128’, proxy_headers = headers)
    # r = proxy.request(’GET’, ’http: // example.com /’)
    # r.status

    #urllib3.ProxyManager( "http://webapi.http.zhimacangku.com/getip?num=400&type=1&pro=&city=0&yys=0&port=1&pack=214550&ts=0&ys=0&cs=0&lb=1&sb=0&pb=5&mr=1&regions=")
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
    req = Request(url=url, headers=headers)
    response = urlopen(req)
    html = response.read().decode("utf-8")
   # print(html)
    return html


def searchEle(html, xpath_exp):

    tree = etree.HTML(html)
    res = tree.xpath(xpath_exp)

   # res = tree.xpath("//a")

    return res


def matchKeyword(str):
    keywords = ['中考', '高考', '高一', '高二', '高三', '高中生', '双减', '寒假', '暑假']
    for kw in keywords:
        if str.find(kw) != -1:
            return True
    return False

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://jyj.hengshui.gov.cn/col/col7179/index.html'

module_xpath = "/html/body/div[2]/table/tbody/tr/td[3]/table[2]/tr/td[1]/a"
module_xpath = "//*[@id=\"13543\"]"

sign_xpath = "//*[@id=\"article_info\"]/span[2]"

alist = searchEle(requesttool(url), module_xpath)  # 获取模块下的所有a标签
print(requesttool(url))
print(len(alist))
for i in alist:
    article_name_ = i.xpath('./text()')
    article_url_ = i.xpath('./@href')
    if len(article_url_) > 0 and len(article_name_) > 0:
        article_name = article_name_[0].strip()
        article_url = article_url_[0].strip()
        if len(article_url) >= 0 and len(article_name) >= 0:
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

            # sign_ = searchEle(requesttool(article_url), sign_xpath)
            #
            # if len(sign_) > 0:
            #     sign = sign_[0].xpath('./text()')
            #     if len(sign) > 0:
            #         sign_text = sign[0].strip()

            print(article_name + " " + article_url+" "+sign_text)
#/html/body/div[3]/div[1]/div/span
# //*[@id="news"]/div[3]/div[1]/div/span