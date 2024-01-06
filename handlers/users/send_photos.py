from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def getfieldPhoto(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def getfile_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("test"))
async def send_test(message: types.Message):
    photo_id = "AgACAgIAAxkBAAOjZZmX_VsJ19A0X2PevbvF8x_xk6gAAkDUMRt3ochIeO5bd-Mj4FkBAAMCAAN4AAM0BA"
    photo_file = InputFile(path_or_bytesio="photos/Photofile.png")
    photo_link = "https://c4.wallpaperflare.com/wallpaper/155/122/485/anime-tokyo-ghoul-re-ken-kaneki-wallpaper-preview.jpg"
    await message.reply_photo(photo_file, caption="Akrom lo'xni rasmi '<b>file</b>'")
    await message.reply_photo(photo_id, caption="Anime id_orqali")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_link)

@dp.message_handler(Command("albom"))
async def send_album(message:types.Message):
    album=types.MediaGroup()
    photo_id = "AgACAgIAAxkBAAOjZZmX_VsJ19A0X2PevbvF8x_xk6gAAkDUMRt3ochIeO5bd-Mj4FkBAAMCAAN4AAM0BA"
    video_link = "BAACAgIAAxkBAAOlZZmYAAGmYCVZnIpiCKjRzBDNGxbcAAK6QgACI_LRSGLgdxR1W3geNAQ"
    photo_file = InputFile(path_or_bytesio="photos/Photofile.png")
    album.attach_photo(photo=photo_id)
    album.attach_video(video=video_link)
    album.attach_photo(photo=photo_file)
    await message.reply_media_group(media=album)