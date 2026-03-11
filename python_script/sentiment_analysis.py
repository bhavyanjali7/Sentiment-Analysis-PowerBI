from textblob import TextBlob
import pandas as pd

data = pd.read_excel("customer_reviews.xlsx")

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

data["Sentiment"] = data["ReviewText"].apply(get_sentiment)

print(data)
