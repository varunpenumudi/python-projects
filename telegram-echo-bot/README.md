# Telegram Bot with Python  

This is a simple Telegram bot built using the `python-telegram-bot` library. The bot can:  

- Respond to the `/hello` command with a personalized greeting.  
- Echo back any text message sent to it.  

## Features  

1. **/hello Command**  
   - Replies with: "Hello {username}"  

2. **Echo Messages**  
   - Repeats the exact message sent by the user.  


## Prerequisites  

1. Python 3.7 or higher.  
2. Telegram Bot API token (obtainable by talking to [BotFather](https://core.telegram.org/bots#botfather) on Telegram).  
3. `python-telegram-bot` library.  
4. `python-dotenv` library for loading the API token securely from an `.env` file.  

## Installation  

1. **Clone the repository:**  

   ```bash  
   git clone https://github.com/varunpenumudi/python-projects.git  
   ```

   ```bash
   cd python-projects/telegram-echo-bot
   ```  

2. **Install dependencies:**  

   ```bash  
   pip install python-telegram-bot python-dotenv  
   ```  

3. **Create a `.env` file:**  

   - Add your Telegram Bot token to the `.env` file:  

     ```env  
     TOKEN=your_telegram_bot_api_token  
     ```  

4. **Run the bot:**  

   ```bash  
   python bot.py  
   ```  

## Usage  

- Start a chat with your bot on Telegram.  
- Use the `/hello` command to receive a personalized greeting.  
- Send any text message, and the bot will echo it back. 

## File Structure  

- `bot.py`: Main script to run the bot.  
- `.env`: File to securely store your Telegram Bot API token (not included in the repo).  

## Libraries Used  

- python-telegram-bot: For building and managing the bot.  
- python-dotenv: For securely handling environment variables.  

## Notes  

- Replace `your_telegram_bot_api_token` in the `.env` file with your actual token from BotFather.  
- Make sure the bot is started on Telegram after being created via BotFather.  
