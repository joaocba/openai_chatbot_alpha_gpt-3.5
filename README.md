## Chatbot AI Assistant (Native)

#### Technology: OpenAi
#### Method: Completions (gpt3.5 turbo model)

#### Description:
Chatbot developed with Python and Flask that features conversation with a virtual assistant. This uses the native conversation stream without any local or indexed context but powered by the new GPT3.5-Turbo model which is cheaper and faster than the other available models for chat. It allows to define an initial role and personification.

### How to run (commands Windows terminal with Python 2.7):

#### Part One: Prepare Environment
- **Define necessary parameters (OpenAi API key, ...) on file 'app.py'**
- Initialize virtual environment and install dependencies, run:

	    virtualenv env
	    env\Scripts\activate
	    pip install flask python-dotenv
        pip install openai

#### Part Two: Run the app

- Initialize the app:

	    flask run

- Enter "http://localhost:5000" on browser to interact with app

#### Changelog
- v0.1
	- initial build