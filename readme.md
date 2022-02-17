### 1、环境
python3.8
### 2、pip安装包
```
lxml==4.7.1
PyMySQL==1.0.2
urllib3==1.26.8
```
### 3、结果落地表
```sql
create table `t_hebei_newslist_spider_result`(
    `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增主键',
    `site_type` varchar(50) NOT NULL COMMENT '站点类型',
    `site_name` varchar(50) NOT NULL COMMENT '站点名称',
    `module_name` varchar(50) NOT NULL COMMENT '站点名称',
    `site_url` varchar(255) NOT NULL COMMENT '站点网址',
    `news_title` varchar(255) NOT NULL COMMENT '新闻标题',
    `news_url` varchar(255) NOT NULL COMMENT '新闻网址',
    `news_date` varchar(20) NOT NULL COMMENT '新闻日期',
    `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `update_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uniq_news` (`news_url`)
)  ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='河北教育新闻爬虫结果表';
```
### 4、配置修改
+ path:   /spider/conf/conf.ini
+ 修改数据库配置 以及 代理获取程序即可。
+ 当前代码中代理ip获取后，使用"/r/n"分割。如需要修改，可在spider/tools.py line:33处修改
