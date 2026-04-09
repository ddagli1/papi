import discord
from discord.ext import commands
from logic import api
from config import TOKEN
import os

# Botun başlatılması
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Kısa mesajların işlenmesi
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    prompt = message.content

    # Görüntüyü ImgAPI aracılığıyla oluşturma
    file_path = api.download_image(prompt)

    # Görüntüyü kullanıcıya gönderme
    with open(file_path, "rb") as photo:
        await message.channel.send(file=discord.File(photo, "generated_image.jpg"))

    # Gönderildikten sonra görüntüyü silme
    os.remove(file_path)

# Bot'u çalıştırma
bot.run(TOKEN)

