from transformers import pipeline

# Sentiment Classification
sentiment_classifier = pipeline("sentiment-analysis")
# Positive
query = "I'm so excited to be learning about large language models"
print(query)
classification = sentiment_classifier(query)

print(classification)

# Negative
query = "I did not get parking in the cinema hall"
print(query)
classification = sentiment_classifier(query)

print(classification)


query = "I went to see a movie movie was not good"
print(query)
classification = sentiment_classifier(query)

print(classification)




