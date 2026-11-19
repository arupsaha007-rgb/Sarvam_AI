import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
sarvam_api_key = os.getenv('SARVAM_API_KEY')

if openai_api_key:
    print("OpenAI API Key is set")
else:
    print("OpenAI API Key not set")
    
if sarvam_api_key:
    print("Sarvam API Key is set")
else:
    raise ValueError("Set SARVAM_API_KEY in your .env file before running this script.")

openai = OpenAI()
sarvam_url ="https://api.sarvam.ai/v2"
sarvam = OpenAI(api_key=sarvam_api_key, base_url=sarvam_url)


OPENAI_MODEL = "gpt-5-nano"
SARVAM_MODEL = "sarvam-105b"

# Write the system prompt
system_prompt = """
Your task is to convert Python code into high performance Java code.
Respond only with Java code. Do not provide any explanation other than occasional comments.
The Java response needs to produce an identical output in the fastest possible time.
"""

# User Prompt
def user_prompt_for(python):
    return f"""
Port this Python code to Java with the fastest possible implementation that produces
 identical output in the least time.
Your response will be written to a file called main.java 

Respond only with Java code.
Python code to port:

```python
{python}
```
"""

def messages_for(python):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(python)}
    ]


def write_output(java,model):
    filename ="main" + model + ".java"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(java)

def port(client, model, python):
    reasoning_effort = "high" if 'gpt' in model else None
    response = client.chat.completions.create(model=model, messages=messages_for(python), reasoning_effort=reasoning_effort)
    reply = response.choices[0].message.content
    # reply = reply.replace('```cpp','').replace('```','')
    write_output(reply,model)

pi = """
import time

def calculate(iterations, param1, param2):
    result = 1.0
    for i in range(1, iterations+1):
        j = i * param1 - param2
        result -= (1/j)
        j = i * param1 + param2
        result += (1/j)
    return result

start_time = time.time()
result = calculate(200_000_000, 4, 1) * 4
end_time = time.time()

print(f"Result: {result:.12f}")
print(f"Execution Time: {(end_time - start_time):.6f} seconds")
"""

def run_python(code):
    globals = {"__builtins__": __builtins__}
    exec(code, globals)

# print(run_python(pi))

# port(openai, OPENAI_MODEL, pi)
# print(f"OPENAI used model::{OPENAI_MODEL}")
port(sarvam, SARVAM_MODEL, pi)
print(f"SARVAM used model::{SARVAM_MODEL}")
