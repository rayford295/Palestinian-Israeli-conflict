# -*- coding: utf-8 -*-
"""clean_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1emoiFvZnWVWjN3k5hDf8ZDKxAWZJuI00
"""

import pandas as pd
import re
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer

def yifan_clean_chinese_text(text):
    """
    Cleans Chinese text by keeping only Chinese characters.
    """
    return ''.join(re.findall(r'[\u4e00-\u9fff]+', text))

def yifan_segment_text(text, stopwords, language='Chinese'):
    """
    Segments text using jieba for Chinese or simple split for English and removes stopwords.
    """
    if language == 'Chinese':
        words = jieba.cut(text)
    else:  # English
        words = text.split()
    return ' '.join(word for word in words if word not in stopwords)

def yifan_process_dataset(file_path, language, stopwords):
    """
    Processes the dataset by reading, cleaning, segmenting, and creating a TF-IDF matrix.
    Returns the processed DataFrame and the TF-IDF matrix.
    """
    data = pd.read_csv(file_path)
    text_column = 'title' if 'Google_News' in file_path else 'Content'

    # Ensure the column is treated as string
    data[text_column] = data[text_column].astype(str)

    if language == 'Chinese':
        data['text_cleaned'] = data[text_column].apply(yifan_clean_chinese_text)
    else:  # English
        data['text_cleaned'] = data[text_column].apply(lambda x: x.lower())
        data['text_cleaned'] = data['text_cleaned'].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x))

    data['text_processed'] = data['text_cleaned'].apply(lambda x: yifan_segment_text(x, stopwords, language))
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(data['text_processed'])
    return data, tfidf_matrix

# Define stopwords for Chinese and English
yifan_chinese_stopwords = set(["的", "了", "在", "是", "我", "有", "和", "就", "不", "人", "都", "一", "一个", "上", "也", "很", "到", "说", "要", "去", "你", "会", "着", "没有", "看", "好", "自己", "这"])
yifan_english_stopwords = set(['the', 'and', 'is', 'in', 'to', 'of', 'a', 'for', 'on', 'with', 'as', 'by', 'that', 'this', 'it', 'are', 'at', 'be', 'from', 'or', 'an', 'was', 'will', 'not', 'have', 'has', 'had', 'its', 'it\'s', 'you', 'your', 'they', 'their', 'what', 'which'])

# Process datasets
file_path1 = '/content/Chinese_version_of_Google_News_crawling_yifan.csv'
data1, tfidf_matrix1 = yifan_process_dataset(file_path1, 'Chinese', yifan_chinese_stopwords)
output_path1 = 'preprocessed_Chinese_version_of_Google_News_crawling_yifan.csv'
data1.to_csv(output_path1, index=False)

# English_version_of_Google_News_crawling_yifan.csv
file_path2 = '/content/English_version_of_Google_News_crawling_yifan.csv'
data2, tfidf_matrix2 = yifan_process_dataset(file_path2, 'English', yifan_english_stopwords)
output_path2 = 'preprocessed_English_version_of_Google_News_crawling_yifan.csv'
data2.to_csv(output_path2, index=False)

# Wikipedia_Chinese_version_of_the_Palestinian-Israeli_conflict_yifan.csv
file_path3 = '/content/Wikipedia_Chinese_version_of_the_Palestinian-Israeli_conflict_yifan.csv'
data3, tfidf_matrix3 = yifan_process_dataset(file_path3, 'Chinese', yifan_chinese_stopwords)
output_path3 = 'preprocessed_Wikipedia_Chinese_version_of_the_Palestinian-Israeli_conflict_yifan.csv'
data3.to_csv(output_path3, index=False)

# Wikipedia_English_version_of_the_Palestinian-Israeli_conflict_yifan.csv
file_path4 = '/content/Wikipedia_English_version_of_the_Palestinian-Israeli_conflict_yifan.csv'
data4, tfidf_matrix4 = yifan_process_dataset(file_path4, 'English', yifan_english_stopwords)
output_path4 = 'preprocessed_Wikipedia_English_version_of_the_Palestinian-Israeli_conflict_yifan.csv'
data4.to_csv(output_path4, index=False)