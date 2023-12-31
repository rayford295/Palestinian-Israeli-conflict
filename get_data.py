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

# Define a function to scrape Wikipedia pages
def yifan_scrape_wikipedia_page(url, file_name):
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Request failed, status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all headers and paragraphs
    elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])

    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Type', 'Content'])

        # Write the type and content of each element to the CSV
        for element in elements:
            element_type = element.name
            element_content = element.get_text().strip()
            writer.writerow([element_type, element_content])

    print(f"Wikipedia data has been saved to {file_name}")

# Define a function to save news from Google News RSS feed to a CSV file
def yifan_save_news_to_csv(rss_url, csv_filename):
    response = requests.get(rss_url)
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Request failed, status code: {response.status_code}")
        return

    root = ET.fromstring(response.content)
    news_items = []

    # Parse the RSS feed and extract news items
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

    print(f"Google News data has been saved to {csv_filename}")

# Scrape English Wikipedia page
yifan_scrape_wikipedia_page(
    "https://en.wikipedia.org/wiki/Israeli%E2%80%93Palestinian_conflict",
    "Wikipedia_English_version_of_the_Palestinian-Israeli_conflict_yifan.csv"
)

# Scrape Chinese Wikipedia page
yifan_scrape_wikipedia_page(
    "https://zh.wikipedia.org/zh-cn/%E4%BB%A5%E5%B7%B4%E5%86%B2%E7%AA%81",
    "Wikipedia_Chinese_version_of_the_Palestinian-Israeli_conflict_yifan.csv"
)

# Save English Google News RSS feed
yifan_save_news_to_csv(
    'https://news.google.com/rss/search?q=Israeli-Palestinian+conflict&hl=en-US&gl=US&ceid=US:en',
    'English_version_of_Google_News_crawling_yifan.csv'
)

# Save Chinese Google News RSS feed
yifan_save_news_to_csv(
    'https://news.google.com/rss/search?q=%E5%B7%B4%E4%BB%A5%E5%86%B2%E7%AA%81&hl=zh-CN&gl=CN&ceid=CN:zh-Hans',
    'Chinese_version_of_Google_News_crawling_yifan.csv'
)