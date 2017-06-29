import json
import re
import csv
from urllib import request


class Spider():
    PATTERN = re.compile("'.*'")
    error_file = 'error_log.txt'
    export_file = ''
    package_dict = {}

    def _load_list(self, file_name):
        with open(file_name) as f:
            for package in self.PATTERN.findall(f.read()):
                yield(package.strip("'"))

    def _load_json(self, package_name):
        url = f'https://pypi.python.org/pypi/{package_name}/json'

        print(f'Loading {package_name}...')

        try:
            response = request.urlopen(url)
            return json.loads(response.read())
        except request.HTTPError:
            print('Failed to load ', package_name)

    def _min_date(self, json):

        try:
            return max(json['releases'][release][0]['upload_time'] for release in json['releases'])
        except Exception:
            #print('Exception')
            return '-'

    def load_feed(self, file_name):
        package_list = self._load_list(file_name)
        #self.package_dict = {package : self._min_date(self._load_json(package)) for (package) in package_list}
        #print(list(package_list))

        with open(f'{self.export_file}', 'w', newline='', encoding='utf8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['package','release date'])
            writer.writeheader()

            for package in package_list:
                self.export_package(writer, [package, self._min_date(self._load_json(package))])

    def set_export_file(self, file_name):
        self.export_file = file_name

        #with open(f'{file_name}', 'w', newline='', encoding='utf8') as csvfile:
            #writer = csv.DictWriter(csvfile, fieldnames=['package','release date'])

            #writer.writeheader()

    def export_package(self, writer, package):
        writer.writerow({'package' : package[0], 'release date': package[1]})

    def export_feed(self, file_name):

        with open(f'{file_name}', 'w', newline='', encoding='utf8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['package','release date'])

            writer.writeheader()
            for package in self.package_dict:
                writer.writerow({'package':package, 'release date':self.package_dict[package]})

if __name__ == "__main__":
    spi = Spider()
    spi.set_export_file('export_feed.csv')
    spi.load_feed('packages-simple.html')
    #spi.export_feed('package-dates.csv')

    #url = "https://pypi.python.org/pypi/Scrapy/json"
    #response = request.urlopen(url)
    #data = json.loads(response.read())

    #ver = data['info']['version']

    #print((data['info']['version']))
    #print((data['releases'][ver][0]['upload_time']))

    # Determine the oldest release date of any verison
    #print(min(data['releases'][release][0]['upload_time'] for release in data['releases']))
