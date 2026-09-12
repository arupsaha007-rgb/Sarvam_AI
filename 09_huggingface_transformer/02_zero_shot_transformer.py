from transformers import pipeline
zeroshot_classifier = pipeline("zero-shot-classification", model = "facebook/bart-large-mnli")

query = "one day I will see the world"
print(query)
sequence_to_classify = query
candidate_labels = ['travel', 'cooking', 'dancing']

classification = zeroshot_classifier(sequence_to_classify, candidate_labels)
print(classification)
print("-------------------------------------------------------------------------------------------")

# 
query = "Moving your feet to the beat, spinning with grace, and letting your body speak through rhythm and movement."
print(query)
sequence_to_classify = query
candidate_labels = ['travel', 'cooking', 'dancing']

classification = zeroshot_classifier(sequence_to_classify, candidate_labels)
print(classification)