
from math import ceil
from re import compile
import asyncio

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import *
from userbot.cmdhelp import *
from tandavbot.utils import *
from userbot.Config import Config

deadly_row = Config.BUTTONS_IN_HELP
deadly_emoji = Config.EMOJI_IN_HELP

def button(page, modules):
    Row = deadly_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"{deadly_emoji} " + pair, data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"☜︎︎︎ 𝙱𝙰𝙲𝙺༆", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"༒︎ 𝙲𝙻𝙾𝚂𝙴 ༒︎", data="close"
            ),
            custom.Button.inline(
               f"༆𝙽𝙴𝚇𝚃 ☞︎︎︎", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]
    # Changing this line may give error in bot as i added some special cmds in Deadlybot channel to get this module work...

    modules = CMD_HELP
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "@MafiaBot_Support":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            result = await builder.article(
                f"Hey! Only use .help please",
                text=f"**Rᴜɴɴɪɴɢ Tᴀɴᴅᴀᴠ  Bᴏᴛ**\n\n__Nᴜᴍʙᴇʀ Oғ Pʟᴜɢɪɴs Iɴsᴛᴀʟʟᴇᴅ__ :`{len(CMD_HELP)}`\n**Pᴀɢᴇ:** 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )                                      
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        elif event.text=='':
            result = builder.article(
                "@MafiaBot_Support",
                text="""**Hey! This is [Tᴀɴᴅᴀᴠ Bᴏᴛ](https://t.me/TANDAV_USERBOT_SUPPORT) \nYou can know more about me from the links given below 👇**""",
                buttons=[
                    [
                        custom.Button.url("🔥 CHANNEL 🔥", "https://t.me/TANDAV_X_TEAM"),
                        custom.Button.url(
                            "⚡ GROUP ⚡", "https://t.me/TANDAV_USERBOT_SUPPORT"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "✨ REPO ✨", "https://t.me/TANDAV_USERBOT_SUPPORT"),
                        custom.Button.url
                    (
                            "🔰 TUTORIAL 🔰", "https://t.me/TANDAV_USERBOT_SUPPORT"
                    )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Hᴇʏ Tʜᴇʀᴇ Pʟᴇᴀsᴇ Mᴀᴋᴇ Uʀ Oᴡɴ Tᴀɴᴅᴀᴠ  Bᴏᴛ Aɴᴅ Usᴇ ..Dᴏɴᴛ Usᴇ Mɪɴᴇ  TᴀɴᴅᴀᴠBᴏᴛ ™",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        await event.edit(
            f"**Lᴇɢᴇɴᴅʀʏ Aғ** [TᴀɴᴅᴀᴠBᴏᴛ](https://t.me/TANDAV_USERBOT_SUPPORT) __Wᴏʀᴋɪɴɢ...__\n\n**Nᴜᴍʙᴇʀ Oғ Pʟᴜɢɪɴs Iɴsᴛᴀʟʟᴇᴅ:** `{len(CMD_HELP)}`\n**Pᴀɢᴇ:** {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=False,
        )
        
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await delete_deadly(event,
              "⚜️ Dᴇᴀᴅʟʏ Bᴏᴛ Mᴇɴᴜ Pʀᴏᴠɪᴅᴇʀ Is Cʟᴏsᴇᴅ ⚜️\n\n         **[⭕️ TᴀɴᴅᴀᴠBᴏᴛ™](https://t.me/TANDAV_USERBOT_SUPPORT)", 5, link_preview=False
            )
        else:
            mafia_alert = "Hᴇʟʟᴏ Tʜᴇʀᴇ Pʟᴢ Mᴀᴋᴇ Uʀ Oᴡɴ TᴀɴᴅᴀᴠBᴏᴛ Aɴᴅ Usᴇ Dᴏɴᴛ Usᴇ Mɪɴᴇ Bᴏᴛ. ©  ™"
            await event.answer(mafia_alert, cache_time=0, alert=True)
                            
    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Hᴇʟʟᴏ Tʜᴇʀᴇ Pʟᴢ Mᴀᴋᴇ Uʀ Oᴡɴ TᴀɴᴅᴀᴠBᴏᴛ Aɴᴅ Usᴇ Dᴏɴᴛ Usᴇ Mɪɴᴇ Bᴏᴛ. © TᴀɴᴅᴀᴠBᴏᴛ ™",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [                
                custom.Button.inline(
                    "⚡ " + cmd[0], data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("◀️ ᏴᎪᏟᏦ", data=f"page({page})")])
        await event.edit(
            f"**📗 File:** `{commands}`\n**🔢 Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Hᴇʟʟᴏ Tʜᴇʀᴇ Pʟᴢ Mᴀᴋᴇ Uʀ Oᴡɴ TᴀɴᴅᴀᴠBᴏᴛ Aɴᴅ Usᴇ Dᴏɴᴛ Usᴇ Mɪɴᴇ Bᴏᴛ. © TᴀɴᴅᴀᴠBᴏᴛ ™",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"**📗 File:** `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                result += f"**⚠️ Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
        else:
            result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ️ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🛠 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**🛠 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"**💬 Explanation:** `{command['usage']}`\n\n"
        else:
            result += f"**💬 Explanation:** `{command['usage']}`\n"
            result += f"**⌨️ For Example:** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"
            
        await event.edit(
            result,
            buttons=[
                custom.Button.inline("☜︎︎︎ 𝙱𝙰𝙲𝙺༆", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )
