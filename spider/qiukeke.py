from tools import Tools
from conf.targetList import getTargetList

if __name__ == '__main__':

    t_list = getTargetList()

    result = []

    tool = Tools()

    for line in t_list:
        # #   网站类型    网站名称	抓取版块/Tag	网址
        site_type = line[0]
        site_name = line[1]
        module_name = line[2]
        url = line[3]
        module_xpath = line[4]
        sigh_xpath = line[5]
        codetype = ""
        if len(line)>6:
            codetype=line[6]

        article_list = tool.getss(url, module_xpath, sigh_xpath,codetype)

        if article_list != None:
            for article in article_list:
                article_name = ""
                article_url = ""
                sign_text = ""
                article_name = article[0]
                article_url = article[1]
                sign_text = article[2]

                if article_name.strip() != "" and article_url.strip() != "":
                    result.append([site_type, site_name, module_name, url, article_name, article_url, sign_text])

    for item in result:
        print(item)
