# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 爬取股票信息

import requests
from bs4 import BeautifulSoup
import re


def get_urls(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all("a")
    urls = []
    for link in links:
        try:
            urls.append(link["href"])
        except:
            continue

    return urls


def get_stock_code(urls):
    stock_code_list = []
    for url in urls:
        if re.search(r"s[hz]\d{6}", url):
            stock_code_list.append(re.search(r"s[hz]\d{6}", url).group())
    return stock_code_list


def get_baidu_stock_url(stock_code):
    stock_info_urls = []
    for i in stock_code:
        stock_info_urls.append("https://gupiao.baidu.com/stock/%s.html" % i)
    return stock_info_urls


def get_stock_info(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, "html.parser")

    stock_name = soup.find_all("a", attrs={'class': 'bets-name'})[0]
    print(soup.find_all("a", attrs={'class': 'bets-name'}))
    print(soup.find_all("a", attrs={'class': 'bets-name'})[0])
    print(stock_name.text.strip())

    link = soup.find_all("strong", attrs={'class': '_close'})[0]
    print(link.string)

    div = soup.find_all("div", attrs={'class': 'bets-content'})[0]
    stock_info_name = div.find_all("dt")[1].string

    stock_info_value = div.find_all("dd")[1].string
    print(stock_info_name, stock_info_value)
    with open("e:\\stockinfo.txt", "a") as fp:
        fp.write("股票名称：" + stock_name.text.strip() + "\n")
        fp.write("股票价格：" + link.string + "\n")
        fp.write(stock_info_name + ":" + stock_info_value + "\n")
        fp.write("****************" * 2 + "\n")


urls = get_urls("http://quote.eastmoney.com/stocklist.html")
# print (urls)
stock_code = get_stock_code(urls)
# print (stock_code)
print(get_baidu_stock_url(stock_code))

for url in get_baidu_stock_url(stock_code):
    get_stock_info(url)
