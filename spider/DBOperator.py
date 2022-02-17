#!/usr/bin/python3

import pymysql
from conf.confReader import ConfReader
import configparser


# 打开数据库连接
class DBOpeartor:
    db: pymysql.Connection == None

    def __init__(self):
        confReader = ConfReader()
        self.db = pymysql.connect(host=confReader.dburl,
                                  user=confReader.dbuser,
                                  password=confReader.dbpassword,
                                  database=confReader.database,
                                  port=int(confReader.dbport),
                                  charset=confReader.charset)

    def close(self):
        self.db.close()

    def upsert(self, tablename, columns, data):
        cursor = self.db.cursor()
        sql = "replace into %s(%s,%s,%s,%s,%s,%s,%s) values('%s','%s','%s','%s','%s','%s','%s')" \
              % (tablename
                 , columns[0], columns[1], columns[2], columns[3], columns[4], columns[5], columns[6]
                 , data[0], data[1], data[2], data[3], data[4], data[5], data[6]
                 )
        try:
            # 执行sql语句
            # print(sql)
            cursor.execute(sql)

            # 提交到数据库执行
            self.db.commit()
            return True
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            return False
