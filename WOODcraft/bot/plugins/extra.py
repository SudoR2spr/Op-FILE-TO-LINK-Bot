from WOODcraft.bot import AngelBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
import time
import shutil, psutil
from utils_bot import *
from WOODcraft import StartTime


START_TEXT = """ 🆔 Your Telegram DC Is ⌾≕≻ `{}`  """


@AngelBot.on_message(filters.regex("angel👼"))
async def maintainers(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="🦋 I am Coded By ⌾≕≻ [WOODcraft](https://t.me/Farooq_is_KING)",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Developer💻", url=f"https://t.me/Farooq_is_KING")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)
            
         
@AngelBot.on_message(filters.regex("follow🦋"))
async def follow_user(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<B>🦋 𝐏𝐥𝐞𝐚𝐬𝐞 𝐉𝐨𝐢𝐧 𝐌𝐲 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🦋</B>",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("✜ 𝐉𝐨𝐢𝐧 𝐔𝐩𝐃𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✜", url=f"https://t.me/Opleech")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)
        

@AngelBot.on_message(filters.regex("DC"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True
    )

    
    
@AngelBot.on_message(filters.command("list"))
async def list(l, m):
    LIST_MSG = "🌺 Hi! {} Here is a list of all my commands \n \n ❍⊱≕≻ Tap on command text and copy then send \n \n ❍⊱≕≻ . `start⚡️` \n ❍⊱≕≻ . `list📚` \n ❍⊱≕≻ . `login🔑` \n ❍⊱≕≻ . `follow🦋` \n ❍⊱≕≻. `ping📡` \n ❍⊱≕≻ . `status🔥` \n ❍⊱≕≻ . `DC` this tells your telegram dc \n ❍⊱≕≻ . `angel👼` "
    await l.send_message(chat_id = m.chat.id,
        text = LIST_MSG.format(m.from_user.mention(style="md"))
        
    )
    
    
@AngelBot.on_message(filters.regex("ping📡"))
async def ping(b, m):
    start_t = time.time()
    ag = await m.reply_text("....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await ag.edit(f"⌾≕≻ Pong!\n{time_taken_s:.3f} 🔥 ms")
    
    
    
    
@AngelBot.on_message(filters.private & filters.regex("status🔥"))
async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  total, used, free = shutil.disk_usage('.')
  total = get_readable_file_size(total)
  used = get_readable_file_size(used)
  free = get_readable_file_size(free)
  sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
  recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
  cpuUsage = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  botstats = f'<b>⌾≕≻ Bot Uptime ⚡️:</b> {currentTime}\n' \
            f'<b>∝⌾≕≻ Total disk space:</b> {total}\n' \
            f'<b>∝⌾≕≻ Used:</b> {used}\n' \
            f'<b>∝⌾≕≻ Free:</b> {free}\n\n' \
            f'🔥 Data Usage 🔥\n<b>Upload:</b> {sent}\n' \
            f'<b>∝⌾≕≻ Down:</b> {recv}\n\n' \
            f'<b>∝⌾≕≻ CPU:</b> {cpuUsage}%\n' \
            f'<b>∝⌾≕≻ RAM:</b> {memory}%\n' \
            f'<b>∝⌾≕≻ Disk:</b> {disk}%\n\n' \
            f'<b>◆〓◆ ❖ 𝐖𝐃 𝐙𝐎𝐍𝐄 ❖ ™ ◆〓◆</b>'
  await update.reply_text(botstats)
