import logging

from telethon import TelegramClient, events

class Telegram:
    def __init__(self, session_name, api_id, api_hash, bot_token):
        self.session_name = session_name
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_token = bot_token
        self.client = None
        self.chat_callbacks = {}

    async def __aenter__(self):
        self.client = TelegramClient(self.session_name, self.api_id, self.api_hash)
        await self.client.start(
            bot_token=self.bot_token
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.disconnect()

    async def add_listener(self, chat_username: str, callback: callable):
        # add error handling around this
        chat = await self.client.get_entity(chat_username)

        if chat.id not in self.chat_callbacks:
            self.chat_callbacks[chat.id] = []
            
            # Register the event handler
            @self.client.on(events.NewMessage(chats=chat.id))
            async def handler(event):
                for cb in self.chat_callbacks[chat.id]:
                    await cb(event)

        self.chat_callbacks[chat.id].append(callback)

        logging.info(f"Added listener for chat {chat_username}")

    async def start_listening(self):
        print("Started listening for messages")
        await self.client.run_until_disconnected()


    async def send_message(self, chat_id, message):
        await self.client.send_message(chat_id, message)

    async def download_profile_photo(self, entity):
        return await self.client.download_profile_photo(entity)