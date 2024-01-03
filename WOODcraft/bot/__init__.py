# (c) adarsh-goel
# (c) sudor2spr @Opleech
from pyrogram import Client
import pyromod.listen
from ..vars import Var
from os import getcwd

AngelBot = Client(
    name='Web Streamer',
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)

multi_clients = {}
work_loads = {}