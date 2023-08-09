# OPENAI_API

This is an intoduction to using API with OPENAI products (chatgpt, dall-e etc)

If you want to learn in depth: I learned through [this](https://www.udemy.com/share/108w3y3@3fhw0tWsFbGyPGWHxBOSINLbBrv6qkVVzd5H7N6c8rv0Q_itu2frj1BIqx0AMPHirg==/) course.

## HOW TO START
- create account on openai website
- create your own API and copy the key
- create your own .env file and paste the key as:

`API = <your copied key without "">`

- do not share .env file with others (add to .gitignore)
- open 1_first_request.ipynb (in 1_first_request folder)
- install packages inside notebook

In the notebook you will find how to start with API requests and explanations with examples 
about arguments used in these requests. 

## CONTENT

1. 1_first_request
first notebook containing simple prompts/request - completion requests. Using model-davinci-003

2. 2_color_palette
python script taking description about color palette, sending it using davinci 003 model by
API and returning rendered  color palette. Using completion request and Chat API

3. 3_gpt-chatbot
python script with chatbot using gpt-3.5-turbo/gpt-4. CTRL+C exits the script. Additional argument is --personality: it determines personality of a chatbot. Great example of using ChatCompletion API with Python

5. 5_counting_tokens
jupiter notebook explaining how to count tokens and prices per prompt (message to AI model)

6. 6_spotify_playlist
code making for us a playlist on our spotify account via chat gpt. We provide a description of a playlist, code makes the playlist on our spotify account
- jupyter notebook file with Chat Completion request to open ai models
- env file with Spotify client apis and api to openai products (you have to make one for yourself)
- .Readme file with my notes how to create virtual env