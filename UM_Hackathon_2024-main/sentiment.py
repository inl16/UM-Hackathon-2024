import docx
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
nltk.download('vader_lexicon')  # Ensure the tokenizer models are downloaded

def read_text_from_docx(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return ' '.join(full_text)

def sentiment_percentage(text):
    sia = SentimentIntensityAnalyzer()

    sentences = sent_tokenize(text)
    positive_words = negative_words = neutral_words = 0

    for sentence in sentences:
        sentiment_score = sia.polarity_scores(sentence)
        words = word_tokenize(sentence)
        num_words = len(words)

        if sentiment_score['compound'] >= 0.05:
            positive_words += num_words
        elif sentiment_score['compound'] <= -0.05:
            negative_words += num_words
        else:
            neutral_words += num_words

    total_words = positive_words + negative_words + neutral_words
    positive_percentage = (positive_words / total_words) * 100 if total_words > 0 else 0
    negative_percentage = (negative_words / total_words) * 100 if total_words > 0 else 0
    neutral_percentage = (neutral_words / total_words) * 100 if total_words > 0 else 0

    return positive_percentage, negative_percentage, neutral_percentage

def analyze_document_sentiment(filename):
    text = read_text_from_docx(filename)
    positive_pct, negative_pct, neutral_pct = sentiment_percentage(text)
    print(f"Positive: {positive_pct:.2f}%, Negative: {negative_pct:.2f}%, Neutral: {neutral_pct:.2f}%")

# Replace 'path_to_your_document.docx' with the actual path to your Word document
analyze_document_sentiment('website_contents.docx')####give me a file with all of the links that you can give me here 

#####give me the descriptions that you can give me here 
