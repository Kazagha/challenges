import json
import sys
import re
from urllib import request


class Spider():
    PATTERN = re.compile("'.*'")
    error_file = 'error_log.txt'

    def _load_list(self, file_name):
        with open(file_name) as f:
            for package in self.PATTERN.findall(f.read()):
                yield(package.strip("'"))

    def _load_json(self, package_name):
        url = f'https://pypi.python.org/pypi/{package_name}/json'

        try:
            response = request.urlopen(url)
            return json.loads(response.read())
        except request.HTTPError:
            print('Failed to load ', package_name)

    def _min_date(self, json):
        pass

    def load_feed(self, file_name):
        package_list = self._load_list(file_name)
        package_dict = {package : self._load_json(package) for (package) in package_list}

    def export_feed(self, file_name):
        pass

if __name__ == "__main__":
    spi = Spider()
    spi.load_feed('packages-simple.html')

    #url = "https://pypi.python.org/pypi/Scrapy/json"
    #response = request.urlopen(url)
    #data = json.loads(response.read())

    #ver = data['info']['version']

    #print((data['info']['version']))
    #print((data['releases'][ver][0]['upload_time']))

    # Determine the oldest release date of any verison
    #print(min(data['releases'][release][0]['upload_time'] for release in data['releases']))
