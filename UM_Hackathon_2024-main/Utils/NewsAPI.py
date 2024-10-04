"""
This will handle the news API requests and responses.
As well as aid in sending this data to ChatGPT for sentiment analysis.
"""

# Importing the required libraries
import requests
import json
import os
import dotenv
from newsapi import NewsApiClient

# Load the environment variables
dotenv.load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Init
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def get_news(search_term: str = "Bitcoin", pipeline=None) -> json:
    """
    This function will get the news from the News API and return it as a JSON object.
    """
    # /v2/top-headlines
    top_headlines = newsapi.get_everything(q=search_term,
                                            language='en')
    
    sentiments = {"positive": 0, "neutral": 0, "negative": 0}
    total_articles = 0

    if top_headlines["status"] == "ok":
        for article in top_headlines["articles"]:
            content = article["content"]
            if content:
                # Perform sentiment analysis
                result = pipeline(content[:512])  # Limit to first 512 tokens
                sentiment = result[0]["label"]
                if sentiment == "POSITIVE":
                    sentiments["positive"] += 1
                elif sentiment == "NEGATIVE":
                    sentiments["negative"] += 1
                else:  # The Transformers pipeline primarily returns POSITIVE or NEGATIVE
                    sentiments["neutral"] += 1
                total_articles += 1

                # Optional: Print the article title and its sentiment
                # print(f"Title: {article['title']}\nSentiment: {sentiment}\n")

    # Calculate sentiment percentages
    if total_articles == 0:
        return {"positive": 0, "neutral": 0, "negative": 0}
    else:
        sentiment_percentages = {k: (v / total_articles) * 100 for k, v in sentiments.items()}

    return sentiment_percentages
