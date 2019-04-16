# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 爬取携程网有关台湾的游记的网页链接

import requests
from bs4 import BeautifulSoup


def get_urls(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all("a")
    urls = []
    for link in links:
        # print(link)
        try:
            if '台湾' in link.text:
                if link["href"][0] == "/":
                    print(link["href"])
                    urls.append("https://you.ctrip.com/" + link["href"])
                else:
                    urls.append(link["href"])
        except:
            continue

    return urls


urls = get_urls("https://you.ctrip.com/searchsite/Travels?query=%25e5%258f%25b0%25e6%25b9%25be")
# urls = get_urls("http://www.baidu.com")
print(urls)
