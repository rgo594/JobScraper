import scrapy
import json


# "https://www.indeed.com/company/Morris-Heights-Health-Center/jobs/Data-Engineer-04a81557bb51f5fa?fccid=ccb4855061f968a2&vjs=3"

class DescSpider(scrapy.Spider):
    name = "desc"
    start_urls = [
    ]
    with open(r"\Users\rgo59\PycharmProjects\JobScraper\JobScraper\jobs.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    for job in jsonObject:
         start_urls.append('https://www.indeed.com' + job['link'])

    def parse(self, response):
        for job in response.xpath('.//div[contains(@class, "jobsearch-ViewJobLayout")]'):
            yield{
                # 'position': job.xpath('.//h1[contains(@class, "JobInfoHeader-title")]/text()').get(),
                # 'company': job.xpath('.//div[contains(@class, "icl-u-lg-mr--sm icl-u-xs-mr--xs")]/a[@href]/text()').get(),
                # 'qualifications': job.css('li::text').getall()
                'desc': job.getall()

            }
#work
