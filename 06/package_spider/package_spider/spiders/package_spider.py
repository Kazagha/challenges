import scrapy

class PackageSpider(scrapy.Spider):
    name = "package_spider"

    NUM_PACKS_TO_REACH = 100000
    PYPI = 'https://pypi.python.org/simple/'

    def start_requests(self):
        urls = [
                'http://quotes.toscrape.com/page/1/',
                self.PYPI
            ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'packages-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('File saved')

if __name__ == "__main__":
    p = PackageSpider
    print(list(p.start_requests(p)))

# https://pypi.python.org/simple/
# https://pypi.python.org/pypi/1pass/json