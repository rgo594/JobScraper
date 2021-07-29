import scrapy
import json

class DescSpider(scrapy.Spider):
    name = "desc"
    start_urls = [
    ]

    #Indeed Template = 'file:///C:/Users/rgo59/PycharmProjects/JobScraper/IJTempDesc.html',

    with open(r"\Users\rgo59\PycharmProjects\JobScraper\JobScraper\jobs.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    for job in jsonObject:
         start_urls.append('https://www.indeed.com' + job['link'])

    def parse(self, response):
        for job in response.xpath('//body'):
            yield{
                'position': job.xpath('.//h1[contains(@class, "JobInfoHeader-title")]/text()').get(),
                'company': job.xpath('.//div[contains(@class, "icl-u-lg-mr--sm icl-u-xs-mr--xs")]/a/text()').get(),
                'company2': job.xpath('.//div[contains(@class, "icl-u-lg-mr--sm icl-u-xs-mr--xs")]/text()').get(),
                'link': job.xpath('.//div[contains(@id,"originalJobLinkContainer")]/a[@href]/@href').get(),
                'qualifications': job.xpath('.//ul/li/text()').getall(),
                'qualifications2': job.xpath('.//ul/p/text()').getall(),
            }
