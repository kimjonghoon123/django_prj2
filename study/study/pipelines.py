# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql


class StudyPipeline:
    def process_item(self, item, spider):
        return item

class annMySQLPipeline(object):
    def open_spider(self, spider):
        settings = spider.settings
        params = {
            'host': settings.get('MYSQL_HOST', '3.36.124.138'),
            'db': settings.get('MYSQL_DATABASE', 'django'),
            'user': settings.get('MYSQL_USER', 'root'),
            'passwd': settings.get('MYSQL_PASSWORD', '1357'),
            'charset': settings.get('MYSQL_CHARSET', 'utf8mb4'),
        }
        self.conn = pymysql.connect(**params)
        self.c = self.conn.cursor()

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS blog_daumnews(
            id INTEGER NOT NULL AUTO_INCREMENT,
            title CHAR(200) NOT NULL,
            PRIMARY KEY (id)
                )
            ''')
    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        self.c.execute('INSERT INTO blog_daumnews(title, link) values (%(title)s, %(link)s )', dict(item))
        self.conn.commit()
        return item

class youtuMySQLPipeline(object):
    def open_spider(self, spider):
        settings = spider.settings
        params = {
            'host': settings.get('MYSQL_HOST', '3.36.124.138'),
            'db': settings.get('MYSQL_DATABASE', 'django'),
            'user': settings.get('MYSQL_USER', 'root'),
            'passwd': settings.get('MYSQL_PASSWORD', '1357'),
            'charset': settings.get('MYSQL_CHARSET', 'utf8mb4'),
        }
        self.conn = pymysql.connect(**params)
        self.c = self.conn.cursor()

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS blog_youtube(
            id INTEGER NOT NULL AUTO_INCREMENT,
            title CHAR(200) NOT NULL,
            PRIMARY KEY (id)
                )
            ''')
    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        self.c.execute('INSERT INTO blog_youtube(title, link) values (%(title)s, %(link)s )', dict(item))
        self.conn.commit()
        return item

class ulsanMySQLPipeline(object):
    def open_spider(self, spider):
        settings = spider.settings
        params = {
            'host': settings.get('MYSQL_HOST', '3.36.124.138'),
            'db': settings.get('MYSQL_DATABASE', 'django'),
            'user': settings.get('MYSQL_USER', 'root'),
            'passwd': settings.get('MYSQL_PASSWORD', '1357'),
            'charset': settings.get('MYSQL_CHARSET', 'utf8mb4'),
        }
        self.conn = pymysql.connect(**params)
        self.c = self.conn.cursor()

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS blog_ulsanann(
            id INTEGER NOT NULL AUTO_INCREMENT,
            title CHAR(200) NOT NULL,
            PRIMARY KEY (id)
                )
            ''')
    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        self.c.execute('INSERT INTO blog_ulsanann(title, link) values (%(title)s, %(link)s )', dict(item))
        self.conn.commit()
        return item
class yeosuMySQLPipeline(object):
    def open_spider(self, spider):
        settings = spider.settings
        params = {
            'host': settings.get('MYSQL_HOST', '3.36.124.138'),
            'db': settings.get('MYSQL_DATABASE', 'django'),
            'user': settings.get('MYSQL_USER', 'root'),
            'passwd': settings.get('MYSQL_PASSWORD', '1357'),
            'charset': settings.get('MYSQL_CHARSET', 'utf8mb4'),
        }
        self.conn = pymysql.connect(**params)
        self.c = self.conn.cursor()

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS blog_yeosuann(
            id INTEGER NOT NULL AUTO_INCREMENT,
            title CHAR(200) NOT NULL,
            PRIMARY KEY (id)
                ) 
            ''')
    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        self.c.execute('INSERT INTO blog_yeosuann(title, link) values (%s, %s)', dict(item))
        self.conn.commit()
        return item

class busanMySQLPipeline(object):
    def open_spider(self, spider):
        settings = spider.settings
        params = {
            'host': settings.get('MYSQL_HOST', '3.36.124.138'),
            'db': settings.get('MYSQL_DATABASE', 'django'),
            'user': settings.get('MYSQL_USER', 'root'),
            'passwd': settings.get('MYSQL_PASSWORD', '1357'),
            'charset': settings.get('MYSQL_CHARSET', 'utf8mb4'),
        }
        self.conn = pymysql.connect(**params)
        self.c = self.conn.cursor()

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS blog_busanann(
            id INTEGER NOT NULL AUTO_INCREMENT,
            title CHAR(200) NOT NULL,
            PRIMARY KEY (id)
                )
            ''')
    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        self.c.execute('INSERT INTO blog_busanann(title, link) values (%(title)s, %(link)s )', dict(item))
        self.conn.commit()
        return item

class incheonMySQLPipeline(object):
    def open_spider(self, spider):
        settings = spider.settings
        params = {
            'host': settings.get('MYSQL_HOST', '3.36.124.138'),
            'db': settings.get('MYSQL_DATABASE', 'django'),
            'user': settings.get('MYSQL_USER', 'root'),
            'passwd': settings.get('MYSQL_PASSWORD', '1357'),
            'charset': settings.get('MYSQL_CHARSET', 'utf8mb4'),
        }
        self.conn = pymysql.connect(**params)
        self.c = self.conn.cursor()

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS blog_incheonann(
            id INTEGER NOT NULL AUTO_INCREMENT,
            title CHAR(200) NOT NULL,
            PRIMARY KEY (id)
                )
            ''')
    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        self.c.execute('INSERT INTO blog_incheonann(title, link) values (%(title)s, %(link)s )', dict(item))
        self.conn.commit()
        return item

#test_zxf(title, link) VALUES(%s,%s)