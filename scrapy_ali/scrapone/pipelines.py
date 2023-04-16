# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ScraponePipeline:

    def __init__(self):
        self.con = sqlite3.connect('data.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''create table if not exists products(
        sku real primary key,
        name text, 
        price text,
        link text)
        ''')

    def process_item(self, item, spider):
        self.cur.execute(""" INSERT or ignore INTO products VALUES (?,?,?,?) """,
                         (item['sku'], item['name'], item['price'], item['link']))
        self.con.commit()
        return item
