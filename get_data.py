# -*- coding: utf-8 -*-
"""get_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13o9xrjdLFA6CDYYI_tMNz7FDlnP-f4AC
"""

import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import csv

# 函数：爬取维基百科页面
def scrape_wikipedia_page(url, file_name):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"请求维基百科页面失败，状态码：{response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])

    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Type', 'Content'])

        for element in elements:
            element_type = element.name
            element_content = element.get_text().strip()
            writer.writerow([element_type, element_content])

    print(f"维基百科内容已保存到 {file_name}")

# 函数：从Google News RSS feed获取并保存新闻
def save_news_to_csv(rss_url, csv_filename):
    response = requests.get(rss_url)
    if response.status_code != 200:
        print(f"获取Google News数据失败，状态码：{response.status_code}")
        return

    root = ET.fromstring(response.content)
    news_items = []

    for item in root.findall('./channel/item'):
        news_dict = {
            'title': item.find('title').text,
            'link': item.find('link').text,
            'pubDate': item.find('pubDate').text
        }
        news_items.append(news_dict)

    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'link', 'pubDate'])
        writer.writeheader()
        writer.writerows(news_items)

    print(f"Google News内容已保存到 {csv_filename}")

# 爬取维基百科页面
scrape_wikipedia_page(
    "https://en.wikipedia.org/wiki/Israeli%E2%80%93Palestinian_conflict",
    "Wikipedia_English_version_of_the_Palestinian-Israeli_conflict_yifan.csv"
)
scrape_wikipedia_page(
    "https://zh.wikipedia.org/zh-cn/%E4%BB%A5%E5%B7%B4%E5%86%B2%E7%AA%81",
    "Wikipedia_Chinese_version_of_the_Palestinian-Israeli_conflict_yifan.csv"
)

# 保存Google News RSS feed新闻
save_news_to_csv(
    'https://news.google.com/rss/search?q=%E5%B7%B4%E4%BB%A5%E5%86%B2%E7%AA%81&hl=zh-CN&gl=CN&ceid=CN:zh-Hans',
    'Chinese_version_of_Google_News_crawling_yifan.csv'
)
save_news_to_csv(
    'https://news.google.com/rss/search?q=Israeli-Palestinian+conflict&hl=en-US&gl=US&ceid=US:en',
    'English_version_of_Google_News_crawling_yifan.csv'
)