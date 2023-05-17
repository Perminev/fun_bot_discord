from settings import settings
import discord
# import * - это тоже самое, что перечислить все файлы
from bot_logic import gen_pass
from bot_logic import gen_emodji
from bot_logic import flip_coin
from bot_logic import pi

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(command_prefix='$', intents=discord.Intents.default())


# Когда бот будет готов, он напишет в консоли свое название!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Когда бот будет получать сообщение, он будет отправлять в этот же канал какие-то сообщения!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Привет! Я бот!')
    if message.content.startswith('$com'):
        await message.channel.send(' **Список комманд:**')
        await message.channel.send('> `$com - показывает этот список`')
        await message.channel.send('> `$hello - приветствуется`')
        await message.channel.send('> `$smile - генирирует случайное эмодзи`')
        await message.channel.send('> `$pass - генирирует случайный пароль`')
        await message.channel.send('> `$coin - подбрасывает монетку`')
        await message.channel.send('> `$pi - число пи`')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$pi'):
        await message.channel.send(pi())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send("Я не понимаю такую команду!")

client.run(settings["TOKEN"])
