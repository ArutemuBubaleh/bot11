import discord
from discord.ext import commands
from config import settings
from config import rules
from config import links
from config import songlyrics
from config import tracklist
from config import clips
import random
import requests
import json
import os
import discord
import youtube_dl
import os
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
import asyncio
from discord.ext import commands
from Cybernator import Paginator
from discord.ext.commands import has_permissions, MissingPermissions

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
STAS = os.path.join(os.path.dirname(__file__), "bareckiy_photo/")
bareckiypics = [STAS + c for c in os.listdir(STAS)]
PIVO = os.path.join(os.path.dirname(__file__), "rvet_pivo/")
pivogifs = [PIVO + c for c in os.listdir(PIVO)]
helpgif = os.path.join(os.path.dirname(__file__), "helpgif.gif")
ban_list = []
day_list = []
server_list = []
l1, l2, l3, l4 = rules[1], rules[2], rules[3], rules[4]
bot = commands.Bot(command_prefix=settings['prefix'])
lyr1, lyr2, lyr3 = songlyrics["Морячок"], songlyrics["Вампир"], songlyrics["Кризис"]
trc1, trc2, trc3 = tracklist["Морячок"], tracklist["Вампир"], tracklist["Кризис"]
clp1, clp2, clp3 = clips["Морячок"], clips["Вампир"], clips["Кризис"]


@bot.command()
async def meme(ctx):
    try:
        await ctx.message.delete()
        res = requests.get('https://meme-api.herokuapp.com/gimme').json()
        embed = discord.Embed(color=0xff9900, title=res['title'])
        embed.set_author(name=f"Автор: {res['author']}   Очки: {res['ups']}")
        embed.set_image(url=f"{res['url']}")
        embed.set_footer(text='Мем с реддита:')
        await ctx.send(embed=embed)
    except Exception as E:
        print(f'Meme command Error: {E}')
        embed = discord.Embed(color=0xff0000, title='Мемчики не отвечают (')


@bot.command()
async def song(ctx, a, name):
    if a == 'lyrics':
        embed1 = discord.Embed(title='Текст песни:', color=0xFF0000)
        embed1.set_image(url="https://media.tenor.com/images/e58c4ef6c678e9789a38235c97f96bf8/tenor.gif")
        if name == "Морячок":
            embed1.add_field(name='Текст', value=lyr1)
            await ctx.send(embed=embed1)
        if name == "Вампир":
            embed1.add_field(name='Текст', value=lyr2)
            await ctx.send(embed=embed1)
        if name == "Кризис":
            embed1.add_field(name='Текст', value=lyr3)
            await ctx.send(embed=embed1)
    if a == 'track':
        embed1 = discord.Embed(title='Трек:', color=0xFF0000)
        embed1.set_image(url="https://media.tenor.com/images/e58c4ef6c678e9789a38235c97f96bf8/tenor.gif")
        if name == "Морячок":
            embed1.add_field(name='Трек', value=trc1)
            await ctx.send(embed=embed1)
        if name == "Вампир":
            embed1.add_field(name='Трек', value=trc2)
            await ctx.send(embed=embed1)
        if name == "Кризис":
            embed1.add_field(name='Трек', value=trc3)
            await ctx.send(embed=embed1)
    if a == 'clip':
        embed1 = discord.Embed(title='Клип:', color=0xFF0000)
        embed1.set_image(url="https://media.tenor.com/images/e58c4ef6c678e9789a38235c97f96bf8/tenor.gif")
        if name == "Морячок":
            embed1.add_field(name='Клип', value=clp1)
            await ctx.send(embed=embed1)
        if name == "Вампир":
            embed1.add_field(name='Клип', value=clp2)
            await ctx.send(embed=embed1)
        if name == "Кризис":
            embed1.add_field(name='Клип', value=clp3)
            await ctx.send(embed=embed1)


def rules_embed_func(ctx):
    embed1 = discord.Embed(title='Общее', color=0xFF0000)
    embed1.add_field(name='Страница 1/4', value=l1)
    embed1.set_image(url=links['stas_govorit'])

    embed2 = discord.Embed(title='Непосредственно Стас', color=0xFF0000)
    embed2.add_field(name='Страница 2/4', value=l2)
    embed2.set_image(url=links['agressive'])

    embed3 = discord.Embed(title='Приколы', color=0xFF0000)
    embed3.add_field(name='Страница 3/4', value=l3)
    embed3.set_image(url=links['beseda'])

    embed4 = discord.Embed(title='Животные', color=0xFF0000)
    embed4.add_field(name='Страница 4/4', value=l4)
    embed4.set_image(url=links['agressive'])

    embeds = [embed1, embed2, embed3, embed4]
    return embeds


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(693144984362156084)

    role = discord.utils.get(member.guild.roles, id=693148892656566323)
    await member.add_roles(role)
    await channel.send(emb=discord.Embed(discription=f"Пользователь{member.name}теперь СУС"))


@bot.command()
async def staspic(ctx):
    await ctx.send(file=discord.File((random.choice(bareckiypics))))


@bot.command()
async def pivo(ctx):
    await ctx.send(file=discord.File((random.choice(pivogifs))))


@bot.command(pass_context=True)
async def text(ctx, arg):
    await ctx.send(arg)


@bot.event
async def on_ready():
    print('Бот подключен, Валчара')
    print('Я стас Барецкий')
    print('Рву банку пива')
    for guild in bot.guilds:
        print(f'Айди сервера: {guild.id}')


@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9900, title='кот')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@bot.command()
async def dumb_cat(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/288528119525146635/835510008774131732/cat_1.mp4')
    await ctx.send('https://cdn.discordapp.com/attachments/288528119525146635/835510008774131732/cat_2.mp4')
    await ctx.send('https://cdn.discordapp.com/attachments/288528119525146635/835510008774131732/cat_3.mp4')


@bot.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9900, title='пес')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9900, title='лиса')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@bot.command()
async def red_panda(ctx):
    response = requests.get('https://some-random-api.ml/img/red_panda')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9900, title='панда какаята другая')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@bot.command()
async def panda(ctx):
    response = requests.get('https://some-random-api.ml/img/panda')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9900, title='панда')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@bot.command()
async def bird(ctx):
    response = requests.get('https://some-random-api.ml/img/birb')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9900, title='птица')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@bot.command()
async def koala(ctx):
    response = requests.get('https://some-random-api.ml/img/koala')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9900, title='коала')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(
        f'Приветствую, {author.mention}!')


@bot.command()
async def commands(ctx):
    message = await ctx.send(embed=rules_embed_func(ctx)[0])
    page = Paginator(bot, message, only=ctx.author, use_more=False, embeds=rules_embed_func(ctx))
    await page.start()


@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await  ctx.channel.purge(limit=1)

    await member.kick(reason=reason)
    await ctx.send(f"кикнул {member.mention}")


@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await  ctx.channel.purge(limit=1)

    await member.ban(reason=reason)
    await ctx.send(f"забанил {member.mention}")


@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def unban(ctx, member: discord.Member, *, reason=None):
    await  ctx.channel.purge(limit=1)

    await member.unban(reason=reason)
    await ctx.send(f"разбанил {member.mention}")


bot.run(settings['token'])
