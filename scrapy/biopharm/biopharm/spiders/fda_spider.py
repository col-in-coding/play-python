import scrapy
from biopharm.items import BiopharmItem

class FdaSpider(scrapy.Spider):
	name = "fda"

	def start_requests(self):
		urls = [
			'https://www.biopharmcatalyst.com/calendars/fda-calendar'
		]
		for url in urls:
			yield scrapy.Request(url = url, callback=self.parse)

	def parse(self, response):
		items = response.xpath('//table[@class="search-data"]/tbody/tr')

		for item in items:
			ticker = item.xpath('.//a[@class="ticker"]/text()').extract_first()
			price = item.xpath('.//div[@class="price"]/text()').extract_first()
			drug = item.xpath('.//strong[@class="drug"]/text()').extract_first()
			stage = item.xpath('.//td[@class="stage"]/text()').extract_first()
			date_text = item.xpath('.//span[@class="catalyst-date-text"]/text()').extract_first()
			end_date = item.xpath('.//time[@class="catalyst-date"]/text()').extract_first()

			yield BiopharmItem(
				ticker = ticker.strip(),
				price = price.strip().replace("$",""),
				drug = drug.strip(),
				stage = stage.strip(),
				date_text = "" if date_text is None else date_text.strip() + " ",
				end_date = end_date.strip()
				)
