from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

sia = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    negative = sia.polarity_scores(text)['neg']
    positive = sia.polarity_scores(text)['pos']
    neutral = sia.polarity_scores(text)['neu']
    compound = sia.polarity_scores(text)['compound']

    return [negative, positive, neutral, compound]


print(analyze_sentiment("HATE HATE HATE HATE LOVE"))
