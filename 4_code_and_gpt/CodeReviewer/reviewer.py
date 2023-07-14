#basic idea is that I want to take a file and this script and receive
#a review of a code in the file

#libraries
import openai
from dotenv import load_dotenv
import os

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
#request function
def make_review_request(filecontent, model):
    #messages
    messages = [
    {"role": "system", "content": PROMPT}
    , {"role": "user", "content": f"Code review the following file: {filecontent}"}
    ]
    #ChatCompletion
    response = openai.ChatCompletion.create(
        model = model
        , messages = messages
    )

    return response["choices"][0]["message"]["content"]

#make review function
def make_review(file_path, model):
    with open(file_path, 'r') as file:
        content = file.read()
    return make_review_request(content, model)

def main():
    print(make_review("code_to_review.py", "gpt-3.5-turbo"))

if __name__ == "__main__":
    #load API key to OPENAI products
    load_dotenv()
    openai.api_key = os.getenv("API")
    main()