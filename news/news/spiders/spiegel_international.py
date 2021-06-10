import pymongo
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.python.compat import xrange
from datetime import datetime


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    sub_title = scrapy.Field()
    abstract = scrapy.Field()


class NewsArchive(scrapy.Spider):
    name = "spiegel"
    start_urls = [
        "https://www.spiegel.de/international/p%s/" % page for page in xrange(1, 500)
    ]

    def parse(self, response, **kwargs):
        follow_loop = range(1, 45)
        for x in follow_loop:
            item = NewsItem()

            updated_xpath = '//*[@id="Inhalt"]/section/div/section/div['
            updated_xpath += str(x)
            updated_xpath += "]/article/div/div"

            if response.xpath(updated_xpath).get() is not None:
                xpath_title = updated_xpath + "/header/h2/a/span/span/text()"
                item["title"] = response.xpath(xpath_title).get()

                xpath_subtitle = updated_xpath + "/header/h2/a/span/span/span/text()"
                item["sub_title"] = response.xpath(xpath_subtitle).get()

                xpath_abstract = updated_xpath + "/section/a/span/text()"
                item["abstract"] = response.xpath(xpath_abstract).get()

                self.mongodb_connection(item)

    def mongodb_connection(self, item):
        # mongodb server
        myclient = pymongo.MongoClient(
            "mongodb://mongoadmin:secret@localhost:27888/?authSource=admin"
        )

        # database creation
        mydb = myclient["News_Archive"]

        # collection creation
        mycol = mydb["news"]

        now = datetime.now()

        outputdata_GCS = item

        output_crawler_details = {
            "title": outputdata_GCS["title"],
            "sub-title": outputdata_GCS["sub_title"],
            "abstract": outputdata_GCS["abstract"],
            "download_time": now.strftime("%d/%m/%Y %H:%M:%S"),
        }
        # check for existing record
        for i in mycol.find():
            if item["sub_title"] == i["sub-title"]:
                mycol.update_one(
                    {"_id": i["_id"]},
                    {"$set": {"update_time": now.strftime("%d/%m/%Y %H:%M:%S")}},
                )
            else:
                mycol.insert_one(output_crawler_details)
                print("Successfully inserted")


process = CrawlerProcess(get_project_settings())

process.crawl(NewsArchive)

process.start()
