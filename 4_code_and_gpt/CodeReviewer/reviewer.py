#basic idea is that I want to take a file and this script and receive
#a review of a code in the file

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
