from flask import Flask, render_template, request
import openai
import os


# set openai API key
# openai.api_key = ''
# os.environ["OPENAI_API_KEY"] = ''
# in case it is already defined on windows path variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

# array to store conversations
conversation = [{"role": "assistant", "content": "You are a virtual assistant and you speak portuguese."}]  # define initial role

app = Flask(__name__)

# define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def generate_response():
    # get user input and add to conversation
    user_input = request.args.get('msg')
    conversation.append({"role": "user", "content": user_input})

    # retrieve response from openai API
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",    # define AI model
        temperature = 1,            # define creativity in the response
        messages = conversation,    # input prompt
        max_tokens = 250,           # max amount of tokens in the prompt and response
        top_p = 0.9                 # diversity rate
    )

    # add response to conversation
    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})

    # return response
    return str(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    app.run()