import json
from discord.ext import commands
import discord
import asyncio

# receber chave do bot
def chave():
    with open('chave.json', 'r') as arquivo:
        chave_bot = json.load(arquivo)
    return chave_bot['chave']


# receber palavroes de arwui de texto
def palavroes():
    with open('palavrao.txt', 'r') as arquivo:
        proibidos = arquivo.read()
    return proibidos

# configuração do bot
intents = discord.Intents().all()
client = discord.Client(intents=intents)

# menssagem no prompt para indicar que esra online
@client.event
async def on_ready():
    print('''

on

''')


# eventos | comandos
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # verificar toda menssagem
    if message.content != '':
        menssagem = message.content
        menssagem = menssagem.lower()
        menssagem = menssagem.split(' ')
        proibido = palavroes().split('\n')
        # log das mensagens
        print(f'\033[34m\n<{message.author}> {message.content}\033[m')
        for palavra in menssagem:
            for palavrao in proibido:
                if palavra == palavrao:
                    if palavrao == '' or palavrao == ' ':
                        pass

                    else:
                        # deletar palavrao
                        try: await message.delete()
                        except: pass
                        # menssagem enviada caso mandem palavrao
                        await message.channel.send(f'# ⚠️MENSSAGEM OFENCIVA⚠️\n\nmenssagem ofenciva de: {message.author.mention} deletada*!*')

# iniciar bot
client.run(chave())
