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
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}

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


["政府官网", "中华人民共和国教育部", "媒体聚焦", "http://www.moe.gov.cn/jyb_xwfb/s5147/",
 "//*[@id=\"list\"]/li[2]/a", "//*[@id=\"moe-detail-box\"]/div[1]"],

["政府官网", "中国教育考试网", "教育要闻", "http://www.moe.gov.cn/jyb_xwfb/s271/",
 "//*[@id=\"list\"]/li[2]/a", "//*[@id=\"moe-detail-box\"]/div[1]"],

url = "http://jyj.chengde.gov.cn/col/col499/index.html"

module_xpath = "//*[@id=\"4392\"]/script"


sign_xpath = ""

alist = searchEle(requesttool(url), module_xpath)  # 获取模块下的所有a标签
# print(requesttool(url))
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
            sign_ = searchEle(requesttool(article_url), sign_xpath)

            sign_text = "-"

            if len(sign_) > 0:
                sign = sign_[0].xpath('./text()')
                if len(sign) > 0:
                    sign_text = sign[0].strip()

            print(article_name + " " + article_url+" "+sign_text)
#/html/body/div[3]/div[1]/div/span
# //*[@id="news"]/div[3]/div[1]/div/span