import scrapy

class JobsSpider(scrapy.Spider):
    name = "jobs"
    start_urls = [
        'https://www.indeed.com/jobs?q=data%20engineer&l',
    ]

    def parse(self, response):
        jobArr = []
        i = 0
        for job in response.xpath('.//div[@class="job_seen_beacon"]'):
                jobDict = {}
                jobDict['position'] = job.xpath('.//h2[contains(@class,"jobTitle")]//span[@title]/text()').get()
                jobDict['company'] = job.xpath('.//a[@data-tn-element ="companyName"]/text()').get()
                if(jobDict['company'] == None):
                    jobDict['company'] = job.xpath('.//span[@class ="companyName"]/text()').get()
                jobDict['location'] = job.css('div.companyLocation::text').getall()
                jobDict['salary'] = job.xpath('.//span[@class ="salary-snippet"]/text()').get()
                jobArr.append(jobDict)
        for link in response.xpath('.//a[contains(@class, "tapItem")]/@href').getall():
            jobArr[i]['link'] = link
            i += 1

        for i in range(len(jobArr) - 1):
            yield{
                'position': jobArr[i]['position'],
                'company': jobArr[i]['company'],
                'location': jobArr[i]['location'],
                'salary': jobArr[i]['salary'],
                'link': jobArr[i]['link'],
            }



        next_page = response.xpath('//a[@aria-label="Next"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

