import discord
import random
import time

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        time.sleep(2)
        return "ОРЕЛ"
    else:
        time.sleep(2)
        return "РЕШКА"

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

#Основной код

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(command_prefix='$', intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

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
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send("Я не понимаю такую команду!")

client.run("ENTER YOUR TOKEN HERE")
