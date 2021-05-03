from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEJhqRghWPsjqUKSS8_6VmdS7qpU3_lTQAC1wEAAhj9KUQdpq7AObW5uh8E")
    await message.reply_text(
        f"""<b>Hey {message.from_user.first_name}!
\nI can play music in your group's voice chat
And Also I Can Manage Ur Group.. ❤️
\nTo add in your group contact us at @CoffinXsupport.
\nUse the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚪ Support Group ⚪", url="https://t.me/KHUFIYAN_ADDA",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚪ Channel ⚪", url="https://t.me/ABOUTSPRAY"
                    ),
                    InlineKeyboardButton(
                        "⚪ Help ⚪", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        "⚪ Assistant ⚪", url="https://t.me/CoffinXAssistant?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="http://t.me/KHUFIYAN_VC_BOT?sartgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝘏𝘦𝘺 𝘐'𝘮 𝘈𝘭𝘪𝘷𝘦..👻 𝘈𝘯𝘥 𝘙𝘦𝘢𝘥𝘺 𝘛𝘰 𝘗𝘭𝘢𝘺 𝘔𝘶𝘴𝘪𝘤 𝘍𝘰𝘳 𝘠𝘰𝘶 🎛️**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/CoffinX_updates"
                    )
                ],[
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Here Is Cmd Of CoffinXmusic !
╔━━━━━━━━⊰✦⊱━━━━━━━━╗
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
╚━━━━━━━━⊰✦⊱━━━━━━━━╝
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/CoffinX_updates"
                    )
                ],[
                    InlineKeyboardButton(
                        "🚑 Support Group", url="https://t.me/CoffinXsupport"
                    ),
                    InlineKeyboardButton(
                        "➕Add CoffinX in your group➕", url="https://t.me/CoffinXmusic_BoT?startgroup=true"
                    )
                ]
            ]
        )
    )
