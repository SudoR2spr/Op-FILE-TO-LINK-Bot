# (c) adarsh-goel
# (c) sudor2spr @Opleech
import os
import time
import string
import random
import asyncio
import aiofiles
import datetime
from WOODcraft.utils.broadcast_helper import send_msg
from WOODcraft.utils.database import Database
from WOODcraft.bot import AngelBot
from WOODcraft.vars import Var
from pyrogram import filters, Client
from pyrogram.types import Message
db = Database(Var.DATABASE_URL, Var.name)
Broadcast_IDs = {}

@AngelBot.on_message(filters.command("users") & filters.private )
async def sts(c: Client, m: Message):
    user_id=m.from_user.id
    if user_id in Var.OWNER_ID:
        total_users = await db.total_users_count()
        await m.reply_text(text=f"∝⌾≕≻ 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬  𝐢𝐧 𝐁𝐃: {total_users}", quote=True)
        
        
@AngelBot.on_message(filters.command("broadcast") & filters.private  & filters.user(list(Var.OWNER_ID)))
async def broadcast_(c, m):
    user_id=m.from_user.id
    out = await m.reply_text(
            text=f"Broadcast initiated! You will be notified with log file when all the users are notified."
    )
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not Broadcast_IDs.get(broadcast_id):
            break
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    Broadcast_IDs[broadcast_id] = dict(
        total=total_users,
        current=done,
        failed=failed,
        success=success
    )
    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(
                user_id=int(user['id']),
                message=broadcast_msg
            )
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1
            if Broadcast_IDs.get(broadcast_id) is None:
                break
            else:
                Broadcast_IDs[broadcast_id].update(
                    dict(
                        current=done,
                        failed=failed,
                        success=success
                    )
                )
    if Broadcast_IDs.get(broadcast_id):
        Broadcast_IDs.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"∝⌾≕≻ 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞𝐝.... `{completed_in}`\n\n∝⌾≕≻ 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬 {total_users}.\n∝⌾≕≻ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥 {done}, {success} ∝⌾≕≻ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬 𝐀𝐧𝐝  {failed} ∝⌾≕≻ 𝐅𝐚𝐢𝐥𝐞𝐝.",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"∝⌾≕≻ 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞𝐝.... `{completed_in}`\n\n∝⌾≕≻ 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬 {total_users}.\n∝⌾≕≻ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥 {done}, {success} ∝⌾≕≻ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬 𝐀𝐧𝐝  {failed} ∝⌾≕≻ 𝐅𝐚𝐢𝐥𝐞𝐝.",
            quote=True
        )
    os.remove('broadcast.txt')
