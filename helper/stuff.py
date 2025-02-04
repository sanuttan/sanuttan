#    This file is part of the CompressorBot distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.reply(
        f"• Hey, `{ok.user.first_name}` ♥️\n• This is a CompressorBot which can encode videos.\n• It can compress your videos at a high percentage (normally 70%-80%, but it solely depends upon your video's size and other properties).\n• You can generate Samples and Screenshots of your video as well.\n• Last but not the least, you can get all the basic details regarding your video under the tab 'MEDIA INFO'.\n✦ Enn ningalude swontham @sanin_c.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
               Button.url("DEVELOPER", url="https://www.instagram.com/sanin.info/"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "ivde onnulla patiche 🙈🙉"
    )


async def ihelp(event):
    await event.edit(
        "ivde onnulla patiche 🙈🙉",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.edit(
        f"• Hey, `{ok.user.first_name}` ♥️\n• This is a CompressorBot which can encode videos.\n• It can compress your videos at a high percentage (normally 70%-80%, but it solely depends upon your video's size and other properties).\n• You can generate Samples and Screenshots of your video as well.\n• Last but not the least, you can get all the basic details regarding your video under the tab 'MEDIA INFO'.\n✦ Enn ningalude swontham @sanin_c.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
               Button.url("DEVELOPER", url="https://www.instagram.com/sanin.info/"),
            ],
        ],
    )


async def sencc(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "Choose Mode",
        buttons=[
            [
                Button.inline("Default Compress", data=f"encc{key}"),
                Button.inline("Custom Compress", data=f"ccom{key}"),
            ],
            [Button.inline("Back", data=f"back{key}")],
        ],
    )


async def back(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "**What to do**",
        buttons=[
            [
                Button.inline("GENERATE SAMPLE", data=f"gsmpl{key}"),
                Button.inline("SCREENSHOTS", data=f"sshot{key}"),
            ],
            [Button.inline("COMPRESS", data=f"sencc{key}")],
        ],
    )


async def ccom(e):
    await e.edit("Type and send any random name that you would like to name your file.\nDo it fast, time could run out.")
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    chat = e.sender_id
    async with e.client.conversation(chat) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=chat))
        repl = await reply
        if "." in repl.text:
            q = repl.text.split(".")[-1]
            g = repl.text.replace(q, "mkv")
        else:
            g = repl.text + ".mkv"
        outt = f"encode/{chat}/{g}"
        x = await repl.reply(
            f"Custom File Name : {g}\nNow, send a Thumbnail Picture for your video file.\nSend the Thumbnail Picture as **Photo** and not as File.\nDo it fast, time could run out."
        )
        replyy = cv.wait_event(events.NewMessage(from_users=chat))
        rep = await replyy
        if rep.media:
            tb = await e.client.download_media(rep.media, f"thumb/{chat}.jpg")
        elif rep.text and not (rep.text).startswith("/"):
            url = rep.text
            os.system(f"wget {url}")
            tb = url.replace("https://telegra.ph/file/", "")
        else:
            tb = thum
        omk = await rep.reply(f"Thumbnail {tb} Setted Successfully")
        hehe = f"{outt};{dl};{tb};{dtime}"
        key = code(hehe)
        await customenc(omk, key)
