import json
from urllib import request

if __name__ == "__main__":
    url = "https://pypi.python.org/pypi/Scrapy/json"
    response = request.urlopen(url)
    data = json.loads(response.read())

    ver = data['info']['version']

    print((data['info']['version']))
    print((data['releases'][ver][0]['upload_time']))