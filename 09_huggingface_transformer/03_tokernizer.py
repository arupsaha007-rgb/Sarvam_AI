from transformers import AutoTokenizer

model = "bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model)

sentence = "I'm so excited to be learning about large language models"
print(sentence)
input_ids = tokenizer(sentence)

print(f"input_ids :::{input_ids}")

tokens = tokenizer.tokenize(sentence)
print(f"tokens :::{tokens}")
# print(tokens)

token_ids = tokenizer.convert_tokens_to_ids(tokens)
print(f"token_ids :::{token_ids}")
# print(token_ids)


decoded_ids = tokenizer.decode(token_ids)
print(f"decoded_ids :::{decoded_ids}")
# print(decoded_ids)

