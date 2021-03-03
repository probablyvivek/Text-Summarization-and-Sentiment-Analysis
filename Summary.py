#Import Libraries
import nltk as nltk
from textblob import TextBlob
import tkinter as tk
from newspaper import Article
nltk.download('punkt')

#Enter the url
url = "https://www.indiansuperleague.com/features/jamil-does-the-unthinkable-but-doesnt-take-the-credit-for-northeast-united-fcs-success"

#Calling the functions below
article = Article(url)
article.download()
article.parse()
article.nlp()

#Printing
print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Date: {article.publish_date}')
print(f'Summary: {article.summary}')

#Sentiment Analysis
analysis = TextBlob(article.text)
print(round(analysis.polarity),2)
print(f'Sentiment: {"Positive" if analysis.polarity >0 else "negative" if analysis.polarity <0 else "neutral"}')








