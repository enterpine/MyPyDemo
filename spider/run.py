from tools import Tools
from conf.targetList import getTargetList
from DBOperator import DBOpeartor
if __name__ == '__main__':

    t_list = getTargetList()

    result = []

    tool = Tools()

    db_done_lines = 0
    total_lines = 0
    total_len = len(t_list)
    process_index = 1
    for line in t_list:
        # #   网站类型    网站名称	抓取版块/Tag	网址
        print("process "+str(process_index)+" of "+str(total_len))
        process_index = process_index + 1
        site_type = line[0]
        site_name = line[1]
        module_name = line[2]
        url = line[3]
        module_xpath = line[4]
        sigh_xpath = line[5]
        codetype = ""
        if len(line) > 6:
            codetype = line[6]

        datetype = ""
        if len(line) > 7:
            datetype = line[7]

        article_list = tool.getss(url, module_xpath, sigh_xpath, codetype, datetype)

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

    dbOpeartor = DBOpeartor()
    # for item in result:
    #     print(item)
    print("writing to DB ")

    total_lines = len(result)
    for item in result:
        b = dbOpeartor.upsert(tablename="t_hebei_newslist_spider_result", columns=['site_type','site_name','module_name','site_url','news_title','news_url','news_date'],data=item)
        if b == True:
            db_done_lines = db_done_lines + 1

    dbOpeartor.close()
    print("write to DB done."+str(db_done_lines)+"/"+str(total_lines))
