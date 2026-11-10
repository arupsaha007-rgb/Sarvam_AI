# pip install -U transformers accelerate torch


from transformers import pipeline

# Load the NER pipeline
nlp = pipeline("token-classification", model="lfcc/bert-portuguese-ner")
text = "O Tribunal de Contas da União fica localizado em Brasília."
print("-" * 77)
print(f"Input :{text}")
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

