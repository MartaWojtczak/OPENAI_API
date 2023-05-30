import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["API"]
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

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
            user_imput = input(color.GREEN+color.BOLD+"You: "+color.END+color.END)
            messages.append({"role":"user", "content": user_imput})
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo"
                , messages = messages
                ) 
            messages.append(response["choices"][0]["message"].to_dict())
            print(color.DARKCYAN+color.BOLD+"Assistant: "+color.END+color.END, response["choices"][0]["message"]["content"])
        except KeyboardInterrupt:
            print("Exit")
            break 
if __name__ == "__main__":
    main()        