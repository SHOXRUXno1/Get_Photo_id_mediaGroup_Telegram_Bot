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


@dp.message_handler(Command("book"))
async def send_book(message: types.Message):
    photo_id = "AgACAgIAAxkBAAMDZZlbxp7w0ckR9IW3n43DFFaX83EAAovUMRsj8tFIFR8VoxjXTo0BAAMCAAN4AAM0BA"
    photo_link = "https://c4.wallpaperflare.com/wallpaper/155/122/485/anime-tokyo-ghoul-re-ken-kaneki-wallpaper-preview.jpg"
    video_link = "BAACAgIAAxkBAAMFZZlb2eWG6aBAmRb8VIbUTczJnD0AAmpAAAIj8tFIer5Ifx5nxJI0BA"
    photo_file = InputFile(path_or_bytesio="photos/Lo'x.png")
    await message.reply_photo(photo_file, caption="Akrom lo'xni rasmi")
    await message.reply_photo(photo_id, caption="Anime")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_id)



@dp.message_handler(Command("album"))
async def send_album(message:types.Message):
    album=types.MediaGroup()
    photo_id = "AgACAgIAAxkBAAMDZZlbxp7w0ckR9IW3n43DFFaX83EAAovUMRsj8tFIFR8VoxjXTo0BAAMCAAN4AAM0BA"
    photo_link1 = "https://c4.wallpaperflare.com/wallpaper/155/122/485/anime-tokyo-ghoul-re-ken-kaneki-wallpaper-preview.jpg"
    video_link2 = "BAACAgIAAxkBAAMFZZlb2eWG6aBAmRb8VIbUTczJnD0AAmpAAAIj8tFIer5Ifx5nxJI0BA"
    photo_file = InputFile(path_or_bytesio="photos/Lo'x.png")
    album.attach_photo(photo=photo_id)
    album.attach_photo(photo=photo_link1)
    album.attach_photo(photo=video_link2)
    album.attach_photo(photo=photo_file)
    await message.reply_media_group(media=album)