This project is a fun AI-powered assistant that can:

1. Generate a custom recipe based on the ingredients you have!

2. Chat with users through a Telegram bot, powered by OpenAI's GPT-3.5!

-Features
1. Web Recipe Generator
Built with Flask and Bootstrap
Enter your ingredients → Get a step-by-step recipe with:
A fun recipe name
A funny version of the name
A fun fact at the end
AI-powered using OpenAI's GPT-3.5 Turbo

2. Telegram Chatbot
Talk to your very own ChatGPT-like bot
Built using aiogram for async handling
Replies intelligently to your questions

-Tech Stack
Feature	Tech Used
Backend (API)	Flask
Frontend	HTML + Bootstrap
AI	OpenAI GPT-3.5
Chatbot Framework	aiogram (for Telegram)
Hosting	Can run on Replit or locally
Code Packaging	Poetry (Python package manager)

-Installation & Usage
1. Clone the repo
git clone https://github.com/your-username/your-repo.git
cd your-repo

3. Set up Python environment with Poetry
poetry install

5. Set environment variable for OpenAI
Create a .env file or set it directly:
export OPENAI_API_KEY=your-openai-api-key

4. Run the Flask App (Recipe Generator)
poetry run python app.py
Then open http://localhost:8080 in your browser.

5. Run the Telegram Bot
Replace the placeholder token in the Telegram code:
bot = Bot(token='your-telegram-bot-token')
Then run:
poetry run python telegram_bot.py

Example Use
-On Web:
I entered: Potato, Cheese, Bread
It gave me a recipe called:
Cheesy Potato Bread Bombs
a.k.a. Boom Boom Tato Toast 
Followed by full steps + a fun food fact!

-On Telegram:
I said: Tell me a joke
Bot replied with a clever GPT-style joke!

Notes
You need an OpenAI API key for both tools to work.
Telegram bot must be connected to a real bot token.
You can deploy this on Replit or use any Python hosting platform.

Future Ideas
-Add recipe images using AI image generation
-Make Telegram bot generate recipes too
-Save recipes to a database or share via links

