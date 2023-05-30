import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["API"]

def main():
    parser = argparse.ArgumentParser(description = "Simple command line chatbot with gpt_3.5-turbo")
    parser.add_argument("--personality"
                        , type = str
                        , help = "a brief summary of the chatbot's personality"
                        , default="friendly chatbot")

    args = parser.parse_args()
    initial_message = f"You are a conversational chatbot. Your personality is: {args.personality}"
    messages = [{"role":"system", "content": initial_message}]
    while True:
        try:
            user_imput = input("You: ")
            messages.append({"role":"user", "content": user_imput})
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo"
                , messages = messages
                ) 
            messages.append(response["choices"][0]["message"].to_dict())
            print("Assistant: ", response["choices"][0]["message"]["content"])
        except KeyboardInterrupt:
            print("Exit")
            break 
if __name__ == "__main__":
    main()        