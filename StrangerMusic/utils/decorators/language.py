from pyrogram.types import Message,CallbackQuery
from strings import get_string
from StrangerMusic.misc import SUDOERS
from StrangerMusic.utils.database import (get_lang, is_commanddelete_on,
                                       is_maintenance)


def language(mystic):
    async def wrapper(_, message:Message, **kwargs):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    "Bot is under maintenance. Please wait for some time... \n Untill use our other bots and enjoy music \n @fallen_MusicBot \n@Sykkunobot"
                )
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery:CallbackQuery, **kwargs):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    "Bot is under maintenance. Please wait for some time... \n Untill use our other bots and enjoy music \n @fallen_MusicBot \n@Sykkunobot",
                    show_alert=True,
                )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, CallbackQuery, language)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message:Message, **kwargs):
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper
