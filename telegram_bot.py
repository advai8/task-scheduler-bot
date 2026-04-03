import schedule
import time
import asyncio
from datetime import datetime
from telegram import Bot

TOKEN = "8711511086:AAEl0AukV2PkNLj1bkukJxRNmPpIxwulrNQ"
CHAT_ID = "8377866648"

bot = Bot(token=TOKEN)

async def send_reminder(task):
    message = f"⏰ Reminder: {task}\nTime: {datetime.now().strftime('%H:%M:%S')}"
    await bot.send_message(chat_id=CHAT_ID, text=message)

import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def job(task):
    loop.run_until_complete(send_reminder(task))

def main():
    print("🤖 Telegram Task Scheduler Bot Started")

    while True:
        task = input("\nEnter task (or 'exit'): ")

        if task.lower() == "exit":
            break

        seconds = int(input("Remind after (seconds): "))

        schedule.every(seconds).seconds.do(job, task)
        print("✅ Reminder scheduled!")

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()