import scrapy
from new_project.items import Headline

class QiitaSpider(scrapy.Spider):
    name = "qiita"
    allowed_domains = ["qiita.com"]
    start_urls = ["https://qiita.com"]

    # def parse(self, response):
    #     res_url = response.css('.style-1p44k52 article').getall()

    #     for url in res_url:
    #         yield response.follow(url, self.parse_topics)

    def parse(self, response):
        item = Headline()
        
        
        for res in response.css('article.style-1w7apwp'):
            yield{
                'author': res.css('p.style-cnjgtl').xpath('string()').get(), 
                'title': res.css('h2.style-1ws5e6r a::text').get(), 
                'date': res.css('span.style-hl9vr4').xpath('string()').get()
            }
            
