import configparser


class ConfReader:
    path = ""
    dburl = ""
    dbuser = ""
    dbpassword = ""
    proxyApiUrl = ""
    database = ""

    dbport = ""
    dbcharset = ""

    def __init__(self):
        path = '/Users/jinsong/PycharmProjects/MyPyDemo/spider/conf/conf.ini'
        config = configparser.ConfigParser()  # 类实例化
        config.read(path)

        self.dburl = config.get('db', 'host')
        self.dbuser = config.get('db', 'user')
        self.dbpassword = config.get('db', 'password')
        self.database = config.get('db', 'database')
        self.dbport = config.get('db', 'port')
        self.charset = config.get('db', 'charset')

        self.proxyApiUrl = config.get('resource', 'proxyApiUrl')
