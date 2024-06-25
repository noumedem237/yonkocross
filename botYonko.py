import asyncio
from datetime import datetime, timedelta
from telethon import TelegramClient, events
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Les détails de votre compte et de votre application Telegram
api_id = '26512330'  # Remplacez par votre propre api_id
api_hash = 'fd7387fc0e42b847f391cd085de20b6f'  # Remplacez par votre propre api_hash
phone_number = '+237691155534'  # Votre numéro de téléphone
#https://t.me/+44a0cdlqZGU3NGY0
# CHAT_ID = "@tessiple"
CHAT_ID = "https://t.me/+Cv1E-4EZPBs2ZmY8"
# CHAT_ID = "https://t.me/+Cv1E-4EZPBs2ZmY8"

client = TelegramClient(phone_number, api_id, api_hash)

async def send_scheduled_message_1():
    message = f'/s 1 for 7min'
    await client.send_message(CHAT_ID, message)

async def job_1():
    await send_scheduled_message_1()

start_time_input = "10:00"
start_time = datetime.strptime(start_time_input, "%H:%M")
start_date_relative = datetime.now() + timedelta(seconds=(start_time - datetime.now()).seconds) - timedelta(hours=1)

scheduler = AsyncIOScheduler()

# Tâche pour le message 1
scheduler.add_job(job_1, 'interval', minutes=10, start_date=start_date_relative, end_date=start_date_relative + timedelta(hours=72))

# Lancer la boucle d'événements de manière asynchrone
async def start_scheduler():
    scheduler.start()
    print("Scheduler started")
    await asyncio.Event().wait()  # Attendre indéfiniment

if __name__ == '__main__':
    client.start()
    client.loop.run_until_complete(start_scheduler())

