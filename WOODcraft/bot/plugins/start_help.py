#WOODcraft goel
from WOODcraft.bot import AngelBot
from WOODcraft.vars import Var
import logging
logger = logging.getLogger(__name__)
from WOODcraft.bot.plugins.stream import MY_PASS
from WOODcraft.utils.human_readable import humanbytes
from WOODcraft.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from WOODcraft.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

                      
@AngelBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        await m.reply_photo(
            photo="https://graph.org/file/948fc22cf79a6d0a4d210.jpg",
            caption="**💐 ʜᴇʟʟᴏ...🤍\n\n❍⊱≕≻ ɪᴀᴍ ᴀ sɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.**\n\n**❍⊱≕≻ ᴜsᴇ /help ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛAɪʟs\n\n❍⊱≕≻ sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ...**",
            reply_markup=InlineKeyboardMarkup(
                [
                   [InlineKeyboardButton("✢ 𝐎𝐰𝐧𝐞𝐫 ✢", url="https://t.me/Farooq_is_KING"), InlineKeyboardButton("✜ 𝐔𝐩𝐃𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✜", url="https://t.me/Opleech")],
                    [InlineKeyboardButton("✜ 𝐃𝐞𝐩𝐥𝐨𝐲 𝐆𝐨 ✜", url="https://www.buymeacoffee.com/woodcraftop"), InlineKeyboardButton("✜ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ✜", url="https://t.me/WD_Topic_Group")],
                ]
            ),
            
        )
    else:

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        msg_text = "**ᴛᴏᴜʀ ʟɪɴᴋ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ...⚡\n\n📧 ғɪʟᴇ ɴᴀᴍᴇ :-\n{}\n {}\n\n💌 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :- {}\n\n♻️ ᴛʜɪs ʟɪɴᴋ ɪs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀɴᴅ ᴡᴏɴ'ᴛ ɢᴇᴛ ᴇxᴘɪʀᴇᴅ ♻️\n\n<b>❖ YouTube.com/@Woodcraft5</b>**"
        await m.reply_text(            
            text=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ⚡", url=stream_link)]])
        )


@AngelBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
              
    await message.reply_photo(
            photo="https://graph.org/file/948fc22cf79a6d0a4d210.jpg",
            caption="**❍⊱≕≻ sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛʜᴇɴ ɪ ᴡɪʟʟ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ɪᴛ...\n\n❍⊱≕≻ ᴛʜɪs ʟɪɴᴋ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ ᴛᴏ sᴛʀᴇᴀᴍ ᴜsɪɴɢ ᴇxᴛᴇʀɴᴀʟ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀs ᴛʜʀᴏᴜɢʜ ᴍʏ sᴇʀᴠᴇʀs.\n\n❍⊱≕≻ ғᴏʀ sᴛʀᴇᴀᴍɪɴɢ ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴘᴀsᴛᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ.\n\n❍⊱≕≻ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ɪɴ ᴄʜᴀɴɴᴇʟ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ɢᴇᴛ ʀᴇᴀʟᴛɪᴍᴇ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ғᴏʀ ᴇᴠᴇʀʏ ғɪʟᴇs/ᴠɪᴅᴇᴏs ᴘᴏsʏ../\n\n❍⊱≕≻ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :- /about\n\n\n❍⊱≕≻ ᴘʟᴇᴀsᴇ sʜᴀʀᴇ ᴀɴᴅ sᴜʙsᴄʀɪʙᴇ 🦋**", 
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✢ 𝐎𝐰𝐧𝐞𝐫 ✢", url="https://t.me/Farooq_is_KING"), InlineKeyboardButton("✜ 𝐔𝐩𝐃𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✜", url="https://t.me/Opleech")],
                    [InlineKeyboardButton("✜ 𝐃𝐞𝐩𝐥𝐨𝐲 𝐆𝐨 ✜", url="https://www.buymeacoffee.com/woodcraftop"), InlineKeyboardButton("✜ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ✜", url="https://t.me/WD_Topic_Group")],
                ]
            ),
            
        )

@AngelBot.on_message(filters.command('about') & filters.private)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    await message.reply_photo(
            photo="https://graph.org/file/948fc22cf79a6d0a4d210.jpg",
            caption="""<b>🤖 My Details 🦋<a href='https://t.me/TG_Files_Link_v1_bot'>Click Here</a></b>

<b>🌺━━━━━━━⫷ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ⫸</b>
┃
┃❍⊱≕≻<b>𝐒𝐞𝐫𝐯𝐞𝐫 ◉ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ
┣≕≻<b>𝐁𝐨𝐨𝐬𝐭 𝐇𝐞𝐫𝐞 𝐏𝐥𝐳 ◉ <a href='https://t.me/Opleech?boost'>Please 🥺</a></b>
┃❍⊱≕≻<b>𝐅𝐨𝐥𝐥𝐨𝐰 𝐌𝐞 ◉ <a href='https://t.me/Farooq_is_KING'>Click Here</a></b>
┣⪼<b>𝐒𝐞𝐫𝐯𝐞𝐫 ◉ ʜᴇʀᴜᴋᴏ</b>
┃❍⊱≕≻<b>𝐋𝐢𝐛𝐫𝐚𝐫𝐲 ◉ ᴘʏʀᴏɢʀᴀᴍ</b>
┣≕≻<b>𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 ◉ ᴘʏᴛʜᴏɴ 3</b>
┃
<b>🌺━━━━━━━❖ 𝐖𝐃 𝐙𝐎𝐍𝐄 ❖ ™</b>""",
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✢ 𝐎𝐰𝐧𝐞𝐫 ✢", url="https://t.me/Farooq_is_KING"), InlineKeyboardButton("✜ 𝐔𝐩𝐃𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✜", url="https://t.me/Opleech")],
                    [InlineKeyboardButton("✜ 𝐃𝐞𝐩𝐥𝐨𝐲 𝐆𝐨 ✜", url="https://telegra.ph/WOODcraft-Upi-10-19"), InlineKeyboardButton("✜ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ✜", url="https://t.me/WD_Topic_Group")],
                ]
            ),
            
        )
