from bs4 import BeautifulSoup
import requests
from lxml import html


def scrapeer():
    print("welcome enter 'www.o2tvseries.com' ")
    url = input(str())
    r = requests.get(url)
    tree = html.fromstring(r.content)
    cla = tree.xpath('//div[@class="data_list"]/text()')
    E = tree.xpath('//div[@class="data-main"]/text()')
    Latest = tree.xpath('//b/text()')
    Episode = tree.xpath('//b/text()')
    div = tree.xpath('//div/text()')
    end_cla = div = tree.xpath('//div/text()')
    print('NEW_UPDATE:===>',Latest, Episode)

scrapeer()
