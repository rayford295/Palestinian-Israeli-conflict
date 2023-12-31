# -*- coding: utf-8 -*-
"""visualize_results.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r8qgBispnRUtM_77neR8H9iN9rh0Bn1o
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Yifan Analysis 1: Keyword and Word Frequency Analysis Visualization
# Load datasets
file_paths_yifan = {
    "Google_News_English_yifan": "/content/keyword_freq_analysis_English_version_of_Google_News_crawling_yifan.csv",
    "Wikipedia_English_Palestinian_Israeli_Conflict_yifan": "/content/keyword_freq_analysis_Wikipedia_English_version_of_the_Palestinian-Israeli_conflict_yifan.csv"
}
dfs_yifan = {name: pd.read_csv(path) for name, path in file_paths_yifan.items()}

# Visualization 1: Bar Chart - Google News English (Yifan)
df_google_news_english_yifan = dfs_yifan['Google_News_English_yifan']
top_keywords_english_news = df_google_news_english_yifan.nlargest(10, 'Top 10 Word Frequency')
plt.figure(figsize=(12, 6))
plt.bar(top_keywords_english_news['Top 10 Keywords'], top_keywords_english_news['Top 10 Word Frequency'], color='skyblue')
plt.xlabel('Keywords', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('Top 10 Keywords in Google News English Dataset (Yifan)', fontsize=16)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Visualization 2: Word Cloud - Wikipedia English Palestinian-Israeli Conflict (Yifan)
df_wikipedia_conflict_yifan = dfs_yifan['Wikipedia_English_Palestinian_Israeli_Conflict_yifan']
keywords_dict_wikipedia = dict(zip(df_wikipedia_conflict_yifan['Top 10 Keywords'], df_wikipedia_conflict_yifan['Top 10 Word Frequency']))
wordcloud_wikipedia = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(keywords_dict_wikipedia)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_wikipedia, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Wikipedia English Palestinian-Israeli Conflict Dataset (Yifan)', fontsize=16)

# Visualization 3: Pie Chart - Wikipedia English Palestinian-Israeli Conflict (Yifan)
top_keywords_wikipedia_conflict = df_wikipedia_conflict_yifan.nlargest(5, 'Top 10 Word Frequency')
plt.figure(figsize=(8, 8))
plt.pie(top_keywords_wikipedia_conflict['Top 10 Word Frequency'], labels=top_keywords_wikipedia_conflict['Top 10 Keywords'], autopct='%1.1f%%', startangle=140)
plt.title('Top 5 Keywords in Wikipedia English Palestinian-Israeli Conflict Dataset (Yifan)', fontsize=16)

# Display all visualizations
plt.show()


# Yifan Analysis 2: Time Series Analysis Visualization
def yifan_load_and_preprocess_time_series_data(file_path):
    """
    Load and preprocess time series data from a CSV file.
    Args:
    file_path (str): Path to the CSV file containing time series data.
    Returns:
    pandas.DataFrame: Preprocessed DataFrame with time series data.
    """
    df = pd.read_csv(file_path, index_col=0, parse_dates=True)
    df.index = pd.to_datetime(df.index)
    return df

def yifan_create_time_series_visualizations(df, title):
    """
    Create visualizations for time series data.
    Args:
    df (pandas.DataFrame): DataFrame containing time series data.
    title (str): Title for the visualizations.
    """
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df)
    plt.title(f'Yifan - Time Series Analysis for {title}')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

file_paths = [
    '/content/time_series_analysis_Chinese_version_of_Google_News_crawling_yifan.csv',
    '/content/time_series_analysis_English_version_of_Google_News_crawling_yifan.csv'
]

for file_path in file_paths:
    df = yifan_load_and_preprocess_time_series_data(file_path)
    title = file_path.split('/')[-1].split('_')[2]  # Extract title from file name
    yifan_create_time_series_visualizations(df, title)


# Yifan Analysis 3: Text Similarity Analysis Visualization
def yifan_load_and_preprocess_similarity_data(file_path):
    """
    Load and preprocess text similarity data from a CSV file.
    Args:
    file_path (str): Path to the CSV file containing similarity data.
    Returns:
    pandas.DataFrame: Preprocessed DataFrame with similarity scores.
    """
    df = pd.read_csv(file_path)
    return df

def yifan_create_similarity_visualizations(df, title):
    """
    Create visualizations for text similarity analysis data.
    Args:
    df (pandas.DataFrame): DataFrame containing similarity scores.
    title (str): Title for the visualizations.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(df, annot=False, cmap='coolwarm', square=True)
    plt.title(f'Yifan - Text Similarity Heatmap for {title}')
    plt.xlabel('Text Index')
    plt.ylabel('Text Index')
    plt.show()

file_paths = [
    '/content/similarity_analysis_Chinese_version_of_Google_News_crawling_yifan.csv',
    '/content/similarity_analysis_English_version_of_Google_News_crawling_yifan.csv',
    '/content/similarity_analysis_Wikipedia_Chinese_version_of_the_Palestinian-Israeli_conflict_yifan.csv',
    '/content/similarity_analysis_Wikipedia_English_version_of_the_Palestinian-Israeli_conflict_yifan.csv'
]

for file_path in file_paths:
    df = yifan_load_and_preprocess_similarity_data(file_path)
    title = file_path.split('/')[-1].split('_')[2]  # Extract title from file name
    yifan_create_similarity_visualizations(df, title)


# Yifan Analysis 4: Sentiment Analysis Visualization
def yifan_load_and_preprocess_sentiment_data(file_path):
    """
    Load and preprocess sentiment analysis data from a CSV file.

    Args:
    file_path (str): Path to the CSV file containing sentiment data.

    Returns:
    pandas.DataFrame: Preprocessed DataFrame with sentiment scores.
    """
    df = pd.read_csv(file_path)
    return df

def yifan_create_sentiment_visualizations(df, title):
    """
    Create visualizations for sentiment analysis data.

    Args:
    df (pandas.DataFrame): DataFrame containing sentiment scores.
    title (str): Title for the visualizations.
    """
    # Sentiment distribution plot
    plt.figure(figsize=(10, 6))
    sns.histplot(df['sentiment'], kde=True, color='skyblue')
    plt.title(f'Yifan - Sentiment Distribution for {title}')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.show()

    # Box plot for sentiment scores
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df['sentiment'], color='lightgreen')
    plt.title(f'Yifan - Sentiment Score Boxplot for {title}')
    plt.xlabel('Sentiment Score')
    plt.show()

# File paths
file_paths = [
    '/content/sentiment_analysis_Chinese_version_of_Google_News_crawling_yifan.csv',
    '/content/sentiment_analysis_English_version_of_Google_News_crawling_yifan.csv',
    '/content/sentiment_analysis_Wikipedia_Chinese_version_of_the_Palestinian-Israeli_conflict_yifan.csv',
    '/content/sentiment_analysis_Wikipedia_English_version_of_the_Palestinian-Israeli_conflict_yifan.csv'
]

# Process and visualize each file
for file_path in file_paths:
    df = yifan_load_and_preprocess_sentiment_data(file_path)
    title = file_path.split('/')[-1].split('_')[2]  # Extract title from file name
    yifan_create_sentiment_visualizations(df, title)