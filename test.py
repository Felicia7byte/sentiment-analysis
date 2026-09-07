from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

text = "This food is so good"

result = sentiment(text)

print(result)