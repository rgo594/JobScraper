import scrapy


class JobsSpider(scrapy.Spider):
    name = "jobs"
    start_urls = [
        'https://www.indeed.com/jobs?q=data%20engineer&l',
    ]


    def parse(self, response):
        for job in response.xpath('.//div[@class="job_seen_beacon"]'):
            yield{
                'position': job.xpath('.//h2[contains(@class,"jobTitle")]//span[@title]/text()').getall(),
                'company': job.xpath('.//a[@data-tn-element ="companyName"]/text()').getall(),
                'comp2': job.xpath('.//span[@class ="companyName"]/text()').getall(),
                'location': job.css('div.companyLocation::text').getall(),
                'salary': job.xpath('.//span[@class ="salary-snippet"]/text()').get(),
            }

        next_page = response.xpath('//a[@aria-label="Next"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)