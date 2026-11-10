# pip install -U transformers accelerate torch

from transformers import pipeline

# Load the NER pipeline
nlp = pipeline("token-classification", model="dslim/bert-base-NER")

# text = "My name is Wolfgang and I live in Berlin. I work for Google."
text = "Rakesh Gupta paid money to Sijo Francis in Bangalore through ICICI Bank"

print("-" * 77)
print(f"Input: {text}")
print("-" * 77)

ner_results = nlp(text)

for index, result in enumerate(ner_results, start=1):
    print(f"Result {index}:")
    print(f"  Token:      {result['word']}")
    print(f"  Entity:     {result['entity']}")
    print(f"  Confidence: {float(result['score']):.4%}")
    print(f"  Token index: {result['index']}")
    print(f"  Start:      {result['start']}")
    print(f"  End:        {result['end']}")
    print(f"  Text:       {text[result['start']:result['end']]}")
    print("-" * 77)