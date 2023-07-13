#basic idea is that I want to take a file and this script and receive
#a review of a code in the file

#libraries
import openai
from dotenv import load_dotenv
import os

#load API key to OPENAI products
load_dotenv()
openai.api_key = os.getenv("API")

#code to be reviewed

filecontent = """
def function_to_be_reviewed(x, y):
    return x**y
"""

#prompt message
PROMPT = """
You will receive a file's contents as text. 
Generate a code review for the file. 
Indicate what changes should me made to improve code

Aspects taking into consideration
- style
- performance
- readability
- maintainability
- if there are any reputable libraries that could be introduced to improve code

Be kind and constructive. Divide code review into two sections: 
- constructive comments
- positive feedback

For each suggested change, include line numbers to which you are reffering (if you do)
"""

#messages

messages = [
{"role": "system", "content": PROMPT}
, {"role": "user", "content": f"Code review the following file: {filecontent}"}
]
#ChatCompletion

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo"
    , messages = messages
)

print(response["choices"][0]["message"]["content"])