import typing
from textblob import TextBlob  # pylint: disable=E0401

def get(text: str) -> str:
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

if __name__ == "__main__":
    print(get("good"))
