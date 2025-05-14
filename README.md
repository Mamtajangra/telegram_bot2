# Telegram Bot - Forward Message

A lightweight Telegram bot script to forward messages from one user (Person A) to another user (Person B) using the Telegram Bot API.

## How It Works
- The bot uses the Telegram Bot API to forward a specific message from a sender to a recipient.
- The script is configurable with chat IDs and message IDs.
- Includes basic error handling for API requests.

## Requirements
- Python 3.x
- A Telegram bot token (get one from [BotFather](https://core.telegram.org/bots#botfather)).
- Libraries: `requests`, `python-dotenv`

## Setup
1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project directory and add your bot token:
   ```
   BOT_TOKEN=your_telegram_bot_token
   ```

## Usage
1. Open the `forward_message.py` script.
2. Update the following variables:
   - `chat_id`: Chat ID of the recipient (Person B).
   - `from_chat_id`: Chat ID of the sender (Person A).
   - `message_id`: ID of the message to forward.
3. Run the script:
   ```bash
   python forward_message.py
   ```

## Example
```python
chat_id = 123456789  # Replace with recipient's chat ID
from_chat_id = 987654321  # Replace with sender's chat ID
message_id = 42  # Replace with the message ID to forward
```

## Notes
- Ensure the bot has the required permissions to access the chats and forward messages.
- Threading logic is included in the script but is commented out. Uncomment it if you want to send messages concurrently.

## Dependencies
- `requests`: For making HTTP requests to the Telegram API.
- `python-dotenv`: For managing environment variables.

