from flask import Flask, render_template, request
import os
import openai


# set openai API key
openai.api_key = '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'
openai.organization = os.getenv("OPENAI_ORGANIZATION")

# array to store conversations, also define here the role of the AI (systems, assistant, user) and its initial behavior
conversation=[{"role": "assistant", "content": "You are a virtual assistant, your name is Tim and you speak portuguese."}]

app = Flask(__name__)

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def completion_response():
    user_input = request.args.get('msg')
    conversation.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = conversation,
        temperature=1,
        max_tokens=250,
        top_p=0.9
    )

    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    return str(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    app.run()