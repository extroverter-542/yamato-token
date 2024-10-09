#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='t.me/aniverseXsupport_robot'>𝐒ᴀɴJɪ 𝐒αᴍᴀ</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Straw_Hat_Bots'>Cʟɪᴄᴋ Hᴇʀᴇ</a>\n○ ᴘᴀɪᴅ ʙᴏᴛ : <a href='https://t.me/aniverseXsupport_robot'>𝐒ᴀɴJɪ 𝐒αᴍᴀ</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/Adult_Flux'>𝐀ᴅᴜʟᴛ 𝐅ʟᴜx</a>\n○ ᴅᴇᴠʟᴏᴘᴇʀ : <a href='https://t.me/aniverseXsupport_robot'>𝐒ᴀɴJɪ 𝐒αᴍᴀ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [ [ InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://t.me/aniverseXsupport_robot"),
                  InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ" , url= "https://t.me/Straw_Hat_Bots")],
                 [InlineKeyboardButton("Mᴀɪɴ Cʜᴀɴɴᴇʟ",url = "https://t.me/Adult_Flux")],
                    [
                        InlineKeyboardButton("🔙 ʙᴀᴄᴋ ", callback_data = "home"),
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pas
