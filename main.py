#THIS IS GENERATE RECIPE CODE

from boltiotai import openai
import os
from flask import Flask, render_template_string, request

# Set your API key from environment variables
openai.api_key = os.environ['OPENAI_API_KEY']

app = Flask(__name__)

# Function to generate recipe using ingredients
def generate_tutorial(components):

 response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{
   "role": "system",
   "content": "You are a helpful assistant"
  }, {
   "role":
   "user",
   "content":
   f"Suggest a recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: {components}, Haldi, Chilly Powder, Tomato Ketchup, Water, Garam Masala, Oil"
  }])
 return response['choices'][0]['message']['content']


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def hello():
 output = ""
 if request.method == 'POST':
  components = request.form['components']
  output = generate_tutorial(components)
# This is a HTML template for a Custom Recipe Generator web page. It includes a form for users to input a list of ingredients/items they have, and two JavaScript functions for generating a recipe based on the input and copying the output to the clipboard. The template uses the Bootstrap CSS framework for styling.
 return render_template_string(
 '''
    <!DOCTYPE html>
    <html>
      <head>
        <title>Infinite Project Generator</title>
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
          rel="stylesheet"
        />
        <script>
          async function generateTutorial() {
            const components = document.querySelector("#components").value;
            const output = document.querySelector("#output");
            output.textContent = "Cooking a recipe for you...";
            const response = await fetch("/generate", {
              method: "POST",
              body: new FormData(document.querySelector("#tutorial-form")),
            });
            const newOutput = await response.text();
            output.textContent = newOutput;
          }
          function copyToClipboard() {
            const output = document.querySelector("#output");
            const textarea = document.createElement("textarea");
            textarea.value = output.textContent;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand("copy");
            document.body.removeChild(textarea);
            alert("Copied to clipboard");
          }
        </script>
      </head>

      <body>
        <div class="container">
          <h1 class="my-4">Custom Recipe Tutorial Generator</h1>
          <form
            id="tutorial-form"
            onsubmit="event.preventDefault(); generateTutorial();"
            class="mb-3"
          >
            <div class="mb-3">
              <label for="components" class="form-label"
                >Ingredients / Items:</label
              >
              <input
                type="text"
                class="form-control"
                id="components"
                name="components"
                placeholder="Enter the list of Ingredients or items you have e.g. Bread, jam, potato etc. "
                required
              />
            </div>
            <button type="submit" class="btn btn-primary">
              Share with me a tutorial
            </button>
          </form>
          <div class="card">
            <div
              class="card-header d-flex justify-content-between align-items-center"
            >
              Output:
              <button class="btn btn-secondary btn-sm" onclick="copyToClipboard()">
                Copy
              </button>
            </div>
            <div class="card-body">
              <pre id="output" class="mb-0" style="white-space: pre-wrap">
    {{ output }}</pre
              >
            </div>
          </div>
        </div>
      </body>
    </html>
    ''',
                    output=output)


@app.route('/generate', methods=['POST'])

def generate():
 components = request.form['components']
 return generate_tutorial(components)


if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8080)


#here generate receipe code ends



'''
#THIS IS TELEGRAM BOT CODE
import os #lets us access environment variables

from boltiotai import openai #to make ur bot talk like chatgpt

import asyncio #lets python do multiple things at once, like chatting with multiple users at same time without freezing
from aiogram import Bot, Dispatcher, types #bot-lets u create telegram bot, dispatcher-lets u handle messages, types-lets u send messages
from aiogram.filters import CommandStart #lets u start bot with /start or /help command

from example import example #importing example.py file

bot = Bot(token='Replace this with your actual bot token id')

dp = Dispatcher()

openai.api_key = os.environ['OPENAI_API_KEY']

example()


@dp.message(CommandStart(['start', 'help']))
async def welcome(message: types.Message):
  await message.reply('Hello! I am GPT Chat BOT. You can ask me anything :)')


@dp.message()
async def gpt(message: types.Message):
  messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role":"user", "content":message.text}]

  response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

  await message.reply(response['choices'][0]['message']['content'])

async def main():
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(main())
'''






