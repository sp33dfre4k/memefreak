import os

import asyncio
import signal
import logging

from clients.telegram import Telegram

running = True

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def signal_handler(sig, frame):
    global running
    logging.info("Stop signal received. Shutting down...")
    running = False

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

async def main():
    logging.info("Memefreak starting up...")

    async with Telegram(
        session_name='anon',
        api_id=os.environ.get("TELEGRAM_API_ID"),
        api_hash=os.environ.get("TELEGRAM_API_HASH"),
        bot_token=os.environ.get("TELEGRAM_BOT_TOKEN"),
    ) as telegram:
        await telegram.add_listener('@moonshotcoindeploys')
        await telegram.start_listening()

if __name__ == "__main__":
    asyncio.run(main())
