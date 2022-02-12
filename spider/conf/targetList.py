def getTargetList():

    #   网站类型    网站名称	抓取版块/Tag	网址
    baseList = [
       ["政府官网", "中国教育考试网", "教育要闻", "http://www.moe.gov.cn/jyb_sy/sy_jyyw/","/html/body/div[1]/div/div[5]/div[3]/div[2]/div[1]/ul/li/a","/html/body/div[2]/div[5]/div[1]"],
        ["政府官网", "中国教育考试网", "教育部简报", "http://www.moe.gov.cn/jyb_sjzl/s3165/","/html/body/div[1]/div/div[5]/div[2]/div[1]/ul/li/a","/html/body/div[2]/div[5]/div[1]"],
        ["政府官网", "河北省教育厅官网", "河北教育要闻", "http://jyt.hebei.gov.cn/col/1405610764482/index.html","/html/body/div[2]/div[1]/table/tr/td[2]/div/div[3]/div/table/tr/td/a","/html/body/div[2]/div[1]/div[2]/div/div/div[2]"],
        # ["政府官网", "石家庄市教育考试院", "高中学考", "http://www.sjzjyksxx.com.cn/News.aspx?classId=4"],
        # ["政府官网", "石家庄市教育考试院", "普通高考", "http://www.sjzjyksxx.com.cn/News.aspx?classId=4"],
        # ["政府官网", "衡水市教育考试院", "高考学考", "http://www.hseea.net/"],
        # ["政府官网", "唐山市教育考试院", "教育要闻", "http://jiaoyuju.tangshan.gov.cn/tswenguangxin/shijiaoyuju1jyyw/"],
        # ["政府官网", "河北省教育考试院", "普通高考", "http://www.hebeea.edu.cn/html/ptgk/index.html"],
        # ["政府官网", "邯郸市教育局", "公告公示", "https://jyj.hd.gov.cn/moreInfo.aspx?menuId=3945"],
        # ["政府官网", "承德市教育局", "公告公示", "http://jyj.chengde.gov.cn/col/col499/index.html"],
        # ["政府官网", "廊坊市教育局", "公告公示", "http://jyj.lf.gov.cn/?cat=57"],
        # ["权威门户", "阳光高考", "河北省招办最新消息", "https://gaokao.chsi.com.cn/gkxx/zc/ss?regionId=086130000"],
    ]
    return baseList