import json
from urllib import request

def Spider(file_name=None):

    def _load_list(file_name):
        pass

    def _load_json(package_name):
        pass

    def _min_date(json):
        pass

    def load_feed(file_name):
        pass

    def export_feed(file_name):
        pass

if __name__ == "__main__":
    pass

    #url = "https://pypi.python.org/pypi/Scrapy/json"
    #response = request.urlopen(url)
    #data = json.loads(response.read())

    #ver = data['info']['version']

    #print((data['info']['version']))
    #print((data['releases'][ver][0]['upload_time']))

    # Determine the oldest release date of any verison
    #print(min(data['releases'][release][0]['upload_time'] for release in data['releases']))
