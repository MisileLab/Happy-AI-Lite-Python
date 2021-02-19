
import pymongo
import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
import datetime
import psutil
import bs4
import urllib
from urllib.request import urlopen, Request
import random
import typing
import os
import youtube_dl


intents = discord.Intents.default()
intents.members = True
Client = commands.Bot(command_prefix='$', intents=intents, help_command=None)
try:
    f = open('token.txt', 'r')
    TOKEN = f.read()
    f.close()
except:
    print('Github LOL and I will give Test Token')
    f = open('token1.txt', 'r')
    TOKEN1 = f.read()
    f.close()
    f = open('token2.txt', 'r')
    TOKEN2 = f.read()
    f.close()
    TOKEN = str(TOKEN1) + str(TOKEN2)
try:
    f = open('pymongotoken.txt', 'r')
    pymongotoken = f.read()
    f.close()
except:
    print('Github LOL')

status = discord.Game('$도움말 또는 $help로 도움말을 보세요.')

def remove_special_region(origin, tagname):
    for x in origin(tagname):
        try:
            x.decompose()
        except AttributeError:
            pass
    return origin

@Client.event
async def on_ready():
    print('ready')
    await Client.change_presence(status=discord.Status.online, activity=status)

@Client.command()
async def 도움말(ctx):
    await ctx.send('https://www.notion.so/AI-c75843db2de04058bc51f7513bb15635')

@Client.command()
async def help(ctx):
    await ctx.send('https://www.notion.so/AI-c75843db2de04058bc51f7513bb15635')

@Client.command()
async def bot(ctx):
    author = ctx.message.author
    author1 = ctx.message.author.name
    pfp = author.avatar_url
    cpupercentage = str(psutil.cpu_percent()) + '%'
    memoryallpercentage = str(int(psutil.virtual_memory().total)) + 'MB'
    memorynotusepercentage = str(int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)) + 'MB'
    embedbot = discord.Embed(title='봇 정보', description='봇의 정보를 나타내는 메시지')
    embedbot.add_field(name='사용 중인 CPU 퍼센트', value=cpupercentage, inline=True)
    embedbot.add_field(name="RAM 정보", value=memorynotusepercentage + '/' + memoryallpercentage, inline=True)
    embedbot.set_author(name=author1, url='https://github.com/MisileLab', icon_url=pfp)
    embedbot.set_footer(text=todaycalculate())
    await ctx.send(embed=embedbot)

@Client.command()
async def 봇(ctx):
    author = ctx.message.author
    author1 = ctx.message.author.name
    pfp = author.avatar_url
    cpupercentage = str(psutil.cpu_percent()) + '%'
    memoryallpercentage = str(int(psutil.virtual_memory().total)) + 'MB'
    memorynotusepercentage = str(int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)) + 'MB'
    embedbot = discord.Embed(title='봇 정보', description='봇의 정보를 나타내는 메시지')
    embedbot.add_field(name='사용 중인 CPU 퍼센트', value=cpupercentage, inline=True)
    embedbot.add_field(name="RAM 정보", value=memorynotusepercentage + '/' + memoryallpercentage, inline=True)
    embedbot.set_author(name=author1, url='https://github.com/MisileLab', icon_url=pfp)
    embedbot.set_footer(text=todaycalculate())
    await ctx.send(embed=embedbot)

@Client.command()
async def time(ctx):
    await ctx.send(todaycalculate())

@Client.command()
async def 시간(ctx):
    await ctx.send(todaycalculate())

@Client.command()
async def count(ctx):
    true_member_count = len([m for m in ctx.guild.members if not m.bot])
    await ctx.send('현재 서버 인원은 ' + str(true_member_count) + '명입니다.')

@Client.command()
async def 인원(ctx):
    true_member_count = len([m for m in ctx.guild.members if not m.bot])
    await ctx.send('현재 서버 인원은 ' + str(true_member_count) + '명입니다.')

@Client.command()
async def calculate(ctx, arg1, arg2, arg3):
    if arg2 == '+':
        await ctx.send(add(arg1, arg3))
    elif arg2 == '-':
        await ctx.send(subtract(arg1, arg3))
    elif arg2 == 'x' or arg2 == 'X':
        await ctx.send(multiply(arg1, arg3))
    elif arg2 == '/':
        await ctx.send(divide(arg1, arg3))
    else:
        await ctx.send('기호를 잘못 입력했습니다.')

@Client.command()
async def 계산(ctx, arg1, arg2, arg3):
    if arg2 == '+':
        await ctx.send(add(arg1, arg3))
    elif arg2 == '-':
        await ctx.send(subtract(arg1, arg3))
    elif arg2 == 'x' or arg2 == 'X':
        await ctx.send(multiply(arg1, arg3))
    elif arg2 == '/':
        await ctx.send(divide(arg1, arg3))
    else:
        await ctx.send('기호를 잘못 입력했습니다.')

@Client.command()
async def weather(ctx, arg1:str):
    author = ctx.message.author
    author1 = ctx.message.author.name
    pfp = author.avatar_url
    end_location = urllib.parse.quote(arg1 + '+날씨')
    url = 'https://search.naver.com/search.naver?ie=utf8&query=' + end_location
    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html, 'html5lib')
    todaytemperature = str(soup.find('p', class_='info_temperature').find('span',class_='todaytemp').text) + '도'
    lowtemperature = str(soup.find('ul', class_='info_list').find('span', class_='merge').find('span', class_='min').find('span', class_='num').text) + '도'
    hightemperature = str(soup.find('ul', class_='info_list').find('span', class_='merge').find('span', class_='max').find('span', class_='num').text) + '도'
    cast_txt = soup.find('ul', class_='info_list').find('p', class_='cast_txt').text
    misaemungi = soup.find('dl', class_='indicator').find_all('dd')[0].find('span', class_='num').text
    misaemungitext = soup.find('dl', class_='indicator').find_all('dd')[0]
    misaemungitext = remove_special_region(misaemungitext,'span').text
    chomisaemungi = soup.find('dl', class_='indicator').find_all('dd')[1].find('span', class_='num').text
    chomisaemungitext = soup.find('dl', class_='indicator').find_all('dd')[1]
    chomisaemungitext = remove_special_region(chomisaemungitext, 'span').text
    ozone = soup.find('dl', class_='indicator').find_all('dd')[2].find('span', class_='num').text
    ozonetext = soup.find('dl', class_='indicator').find_all('dd')[2]
    ozonetext = remove_special_region(ozonetext, 'span').text
    embedweather = discord.Embed(title='날씨', description='현재 ' + arg1 + '의 날씨', color=0x4f78ff)
    embedweather.add_field(name="현재 온도", value=todaytemperature, inline=True)
    embedweather.add_field(name="최저 온도", value=lowtemperature, inline=False)
    embedweather.add_field(name='최고 온도', value=hightemperature, inline=True)
    embedweather.add_field(name='온도 비교+날씨', value=cast_txt, inline=False)
    embedweather.add_field(name='미세먼지 농도', value=misaemungi, inline=False)
    embedweather.add_field(name='미세먼지 농도 단계', value=misaemungitext, inline=True)
    embedweather.add_field(name='초미세먼지 농도', value=chomisaemungi, inline=False)
    embedweather.add_field(name='초미세먼지 농도 단계', value=chomisaemungitext, inline=True)
    embedweather.add_field(name='오존 농도', value=ozone, inline=False)
    embedweather.add_field(name='오존 농도 단계', value=ozonetext, inline=True)
    embedweather.set_author(name=author1, url='https://github.com/MisileLab', icon_url=pfp)
    embedweather.set_footer(text=todaycalculate())
    await ctx.send(embed=embedweather)

@Client.command()
async def 날씨(ctx, arg1:str):
    author = ctx.message.author
    author1 = ctx.message.author.name
    pfp = author.avatar_url
    end_location = urllib.parse.quote(arg1 + '+날씨')
    url = 'https://search.naver.com/search.naver?ie=utf8&query=' + end_location
    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html, 'html5lib')
    todaytemperature = str(soup.find('p', class_='info_temperature').find('span',class_='todaytemp').text) + '도'
    lowtemperature = str(soup.find('ul', class_='info_list').find('span', class_='merge').find('span', class_='min').find('span', class_='num').text) + '도'
    hightemperature = str(soup.find('ul', class_='info_list').find('span', class_='merge').find('span', class_='max').find('span', class_='num').text) + '도'
    cast_txt = soup.find('ul', class_='info_list').find('p', class_='cast_txt').text
    misaemungi = soup.find('dl', class_='indicator').find_all('dd')[0].find('span', class_='num').text
    misaemungitext = soup.find('dl', class_='indicator').find_all('dd')[0]
    misaemungitext = remove_special_region(misaemungitext,'span').text
    chomisaemungi = soup.find('dl', class_='indicator').find_all('dd')[1].find('span', class_='num').text
    chomisaemungitext = soup.find('dl', class_='indicator').find_all('dd')[1]
    chomisaemungitext = remove_special_region(chomisaemungitext, 'span').text
    ozone = soup.find('dl', class_='indicator').find_all('dd')[2].find('span', class_='num').text
    ozonetext = soup.find('dl', class_='indicator').find_all('dd')[2]
    ozonetext = remove_special_region(ozonetext, 'span').text
    embedweather = discord.Embed(title='날씨', description='현재 ' + arg1 + '의 날씨', color=0x4f78ff)
    embedweather.add_field(name="현재 온도", value=todaytemperature, inline=True)
    embedweather.add_field(name="최저 온도", value=lowtemperature, inline=False)
    embedweather.add_field(name='최고 온도', value=hightemperature, inline=True)
    embedweather.add_field(name='온도 비교+날씨', value=cast_txt, inline=False)
    embedweather.add_field(name='미세먼지 농도', value=misaemungi, inline=False)
    embedweather.add_field(name='미세먼지 농도 단계', value=misaemungitext, inline=True)
    embedweather.add_field(name='초미세먼지 농도', value=chomisaemungi, inline=False)
    embedweather.add_field(name='초미세먼지 농도 단계', value=chomisaemungitext, inline=True)
    embedweather.add_field(name='오존 농도', value=ozone, inline=False)
    embedweather.add_field(name='오존 농도 단계', value=ozonetext, inline=True)
    embedweather.set_author(name=author1, url='https://github.com/MisileLab', icon_url=pfp)
    embedweather.set_footer(text=todaycalculate())
    await ctx.send(embed=embedweather)

@Client.command()
async def 랭크(ctx, target:typing.Optional[discord.Member]):
    target = target or ctx.author
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='leveling')
    author = target.id
    author1 = ctx.message.author
    pfp = author1.avatar_url
    author2 = author1.name
    filter1 = {"_id":author}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":author, "name":author1, "exp":0, "level":1}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        embedlevel = discord.Embed(title='랭크 메시지', color=0xe61526)
        embedlevel.add_field(name='레벨', value=each_doc['level'], inline=True)
        embedlevel.add_field(name='xp', value=each_doc['exp'], inline=True)
        embedlevel.add_field(name='남은 xp', value=multiply(each_doc['level'], 350) - each_doc['exp'], inline=True)
        embedlevel.set_author(name=author2, url='https://github.com/MisileLab', icon_url=pfp)
        embedlevel.set_footer(text=todaycalculate())
        await ctx.send(embed=embedlevel)

@Client.command()
async def rank(ctx, target:typing.Optional[discord.Member]):
    target = target or ctx.author
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='leveling')
    author = target.id
    author1 = ctx.message.author
    pfp = author1.avatar_url
    author2 = author1.name
    filter1 = {"_id":author}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":author, "name":author1, "exp":0, "level":1}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        embedlevel = discord.Embed(title='랭크 메시지', color=0xe61526)
        embedlevel.add_field(name='레벨', value=each_doc['level'], inline=True)
        embedlevel.add_field(name='xp', value=each_doc['exp'], inline=True)
        embedlevel.add_field(name='남은 xp', value=multiply(each_doc['level'], 350) - each_doc['exp'], inline=True)
        embedlevel.set_author(name=author2, url='https://github.com/MisileLab', icon_url=pfp)
        embedlevel.set_footer(text=todaycalculate())
        await ctx.send(embed=embedlevel)


@commands.Cog.listener()
async def on_message(ctx):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='leveling')
    author = ctx.author.id
    author1 = ctx.author.name
    filter1 = {"_id":author}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":author, "name":author1, "exp":0, "level":1}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        level1 = each_doc['level']
        exp1 = int(each_doc['exp']) + random.randint(25, 35)
        if exp1 >= multiply(level1, 350):
            level1 = int(level1) + 1
            exp1 = 0
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)
            ctx.send(f'{ctx.author.name}님이 {level1}레벨으로 레벨업 하였습니다!')
        else:
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)

@Client.event
async def on_member_join(member):
    mod = 749339636270104626
    welcomechannel = await Client.fetch_channel(749446018856386651)
    true_member_count = len([m for m in member.guild.members if not m.bot])
    embed=discord.Embed(title="멤버 입장", description=f'{member.name}이 아이스크림 해피 디스코드에 입장했어요!', color=0x00a352)
    embed.add_field(name='현재 인원', value=str(true_member_count) + '명')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=todaycalculate())
    await member.add_roles(member.guild.get_role(mod))
    await welcomechannel.send(embed=embed)

@Client.event
async def on_member_remove(member):
    welcomechannel = await Client.fetch_channel(749446018856386651)
    true_member_count = len([m for m in member.guild.members if not m.bot])
    embed=discord.Embed(title="멤버 입장", description=f'{member.name}이 아이스크림 해피 디스코드에 나갔어요!', color=0xff4747)
    embed.add_field(name='현재 인원', value=str(true_member_count) + '명')
    embed.set_footer(text=todaycalculate())
    embed.set_thumbnail(url=member.avatar_url)
    await welcomechannel.send(embed=embed)


@Client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("음악이 끝날 때까지 기다리세요.")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@Client.command()
async def leave(ctx):
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("봇이 음성 채널에 들어가있지 않습니다.")


@Client.command()
async def pause(ctx):
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("음악을 틀어놓은게 없습니다.")


@Client.command()
async def resume(ctx):
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("음악이 일시정지되지 않았습니다.")


@Client.command()
async def stop(ctx):
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
    voice.stop()

@Client.command()
async def 재생(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("음악이 끝날 때까지 기다리세요.")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@Client.command()
async def 퇴장(ctx):
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("봇이 음성 채널에 들어가있지 않습니다.")

@Client.command()
async def 시작(ctx):
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("음악이 일시정지되지 않았습니다.")


@Client.command()
async def 정지(ctx):
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
    voice.stop()

@Client.command(name='kick')
@has_permissions(kick_members=True)
async def _kick(ctx, arg1:discord.Member, arg2:typing.Optional):
    arg2 = arg2 or None
    arg1.kick(reason=arg2)
    await ctx.send(f"{arg1.display_name}님이 성공적으로 킥되었습니다. 이유: {arg2}")

@_kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@Client.command(name='킥')
@has_permissions(kick_members=True)
async def _킥(ctx, arg1:discord.Member, arg2:typing.Optional):
    arg2 = arg2 or None
    arg1.kick(reason=arg2)
    await ctx.send(f"{arg1.display_name}님이 성공적으로 킥되었습니다. 이유: {arg2}")

@_킥.error
async def 킥에러(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@Client.command(name='ban')
@has_permissions(ban_members=True)
async def _ban(ctx, arg1:discord.Member):
    arg1.ban()
    await ctx.send(f"{arg1.display_name}님이 성공적으로 밴되었습니다.")

@_ban.error
async def ban에러(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@Client.command(name='밴')
@has_permissions(ban_members=True)
async def _밴(ctx, arg1:discord.Member):
    arg1.ban()
    await ctx.send(f"{arg1.display_name}님이 성공적으로 밴되었습니다.")

@_밴.error
async def 밴에러(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@Client.command(name='격리')
@has_permissions(ban_members=True, kick_members=True, manage_roles=True)
async def _격리(ctx, arg1:discord.Member):
    guild = Client.get_guild(635336036465246218)
    role1 = guild.get_role(749473772817481729)
    role2 = guild.get_role(749446502509707356)
    role3 = guild.get_role(749339636270104626)
    role4 = guild.get_role(802733890221375498)
    await arg1.remove_roles(role1)
    await arg1.remove_roles(role2)
    await arg1.remove_roles(role3)
    await arg1.add_roles(role4)
    await ctx.send(f"{arg1.display_name}님이 성공적으로 격리되었습니다.")

@_격리.error
async def 격리에러(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@Client.command(name='격리해제')
@has_permissions(ban_members=True, kick_members=True, manage_roles=True)
async def _격리해제(ctx, arg1:discord.Member):
    guild = Client.get_guild(635336036465246218)
    role1 = guild.get_role(749339636270104626)
    role2 = guild.get_role(802733890221375498)
    await arg1.add_roles(role1)
    await arg1.remove_roles(role2)
    await ctx.send(f"{arg1.display_name}님이 성공적으로 격리해제 되었습니다.")

@_격리해제.error
async def 격리_에러(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@Client.command(name='mute')
@has_permissions(kick_members=True)
async def _mute(ctx, arg1:discord.Member):
    print('1')
    guild = Client.get_guild(635336036465246218)
    role1 = guild.get_role(749444844178374798)
    await arg1.add_roles(role1)
    await ctx.send(f"{arg1.display_name}님이 성공적으로 뮤트되었습니다.")

@_mute.error
async def mute에러(ctx, error):
    print(error)
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@Client.command(name='뮤트')
@has_permissions(kick_members=True)
async def _뮤트(ctx, arg1:discord.Member):
    guild = Client.get_guild(635336036465246218)
    role1 = guild.get_role(749444844178374798)
    await arg1.add_roles(role1)
    await ctx.send(f"{arg1.display_name}님이 성공적으로 뮤트되었습니다.")

@_뮤트.error
async def 뮤트에러(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@Client.command(name='unmute')
@has_permissions(kick_members=True)
async def _unmute(ctx, arg1:discord.Member):
    guild = Client.get_guild(635336036465246218)
    role1 = guild.get_role(749444844178374798)
    await arg1.remove_roles(role1)
    await ctx.send(f"{arg1.display_name}님이 성공적으로 언뮤트되었습니다.")

@_unmute.error
async def unmute에러(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@Client.command(name='언뮤트')
@has_permissions(kick_members=True)
async def _언뮤트(ctx, arg1:discord.Member):
    guild = Client.get_guild(635336036465246218)
    role1 = guild.get_role(749444844178374798)
    await arg1.remove_roles(role1)
    await ctx.send(f"{arg1.display_name}님이 성공적으로 언뮤트되었습니다.")

@_언뮤트.error
async def 언뮤트에러(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@Client.command
async def warn(ctx, arg1:discord.Member):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='warn')
    ar1 = arg1.name
    ar2 = arg1.id
    filter1 = {"_id":ar2}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":ar2, "name":ar1, "warn":0}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        await ctx.send(f'{arg1.display_name}님의 주의 개수는 {each_doc["warn"]}개입니다.')

@Client.command
async def 주의(ctx, arg1:discord.Member):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='warn')
    ar1 = arg1.name
    ar2 = arg1.id
    filter1 = {"_id":ar2}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":ar2, "name":ar1, "warn":0}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        await ctx.send(f'{arg1.display_name}님의 주의 개수는 {each_doc["warn"]}개입니다.')

@has_permissions(kick_members=True)
@Client.command(name='addwarn')
async def _addwarn(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='warn')
    ar1 = arg1.name
    ar2 = arg1.id
    filter1 = {"_id":ar2}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":ar2, "name":ar1, "warn":0}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ii1 = int(each_doc['warn']) + int(arg2)
        memberdictionary2 = {"_id":ar2, "name":ar1, "warn":ii1}
        clientdictionary.replace_one(filter=filter1, replacement=memberdictionary2)
        await ctx.send(f'{arg1.display_name}님에게 주의를 {arg2}만큼 주었습니다. 현재 주의 개수 {ii1}')

@_addwarn.error
async def warnerror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(kick_members=True)
@Client.command(name='주의추가')
async def _주의추가(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='warn')
    ar1 = arg1.name
    ar2 = arg1.id
    filter1 = {"_id":ar2}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":ar2, "name":ar1, "warn":0}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ii1 = int(each_doc['warn']) + int(arg2)
        memberdictionary2 = {"_id":ar2, "name":ar1, "warn":ii1}
        clientdictionary.replace_one(filter=filter1, replacement=memberdictionary2)
        await ctx.send(f'{arg1.display_name}님에게 주의를 {arg2}만큼 주었습니다. 현재 주의 개수 {ii1}')

@_주의추가.error
async def addwarnerror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(kick_members=True)
@Client.command(name='주의설정')
async def _주의설정(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='warn')
    ar1 = arg1.name
    ar2 = arg1.id
    filter1 = {"_id":ar2}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":ar2, "name":ar1, "warn":0}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    ii1 = int(arg2)
    memberdictionary2 = {"_id":ar2, "name":ar1, "warn":ii1}
    clientdictionary.replace_one(filter=filter1, replacement=memberdictionary2)
    await ctx.send(f'{arg1.display_name}님에게 주의를 {arg2}로 설정했습니다.')

@_주의설정.error
async def setwarnerror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(kick_members=True)
@Client.command(name='setwarn')
async def _setwarn(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='warn')
    ar1 = arg1.name
    ar2 = arg1.id
    filter1 = {"_id":ar2}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":ar2, "name":ar1, "warn":0}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    ii1 = int(arg2)
    memberdictionary2 = {"_id":ar2, "name":ar1, "warn":ii1}
    clientdictionary.replace_one(filter=filter1, replacement=memberdictionary2)
    await ctx.send(f'{arg1.display_name}님에게 주의를 {arg2}로 설정했습니다.')

@_setwarn.error
async def _setwarnerror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(kick_members=True)
@Client.command(name='deletewarn')
async def _deletewarn(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='warn')
    ar1 = arg1.name
    ar2 = arg1.id
    filter1 = {"_id":ar2}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":ar2, "name":ar1, "warn":0}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ii1 = int(each_doc['warn']) - int(arg2)
        memberdictionary2 = {"_id":ar2, "name":ar1, "warn":ii1}
        clientdictionary.replace_one(filter=filter1, replacement=memberdictionary2)
        await ctx.send(f'{arg1.display_name}님에게 주의를 {arg2}만큼 삭제했습니다. 현재 주의 개수 {ii1}')

@_deletewarn.error
async def _deletewarnerror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(kick_members=True)
@Client.command(name='주의삭제')
async def _주의삭제(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='warn')
    ar1 = arg1.name
    ar2 = arg1.id
    filter1 = {"_id":ar2}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":ar2, "name":ar1, "warn":0}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ii1 = int(each_doc['warn']) - int(arg2)
        memberdictionary2 = {"_id":ar2, "name":ar1, "warn":ii1}
        clientdictionary.replace_one(filter=filter1, replacement=memberdictionary2)
        await ctx.send(f'{arg1.display_name}님에게 주의를 {arg2}만큼 삭제했습니다. 현재 주의 개수 {ii1}')

@_주의삭제.error
async def deletewarnerror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(administrator=True)
@Client.command(name='expadd')
async def _expadd(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='leveling')
    author = arg1.id
    author1 = arg1.name
    filter1 = {"_id":author}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":author, "name":author1, "exp":0, "level":1}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ctx.send('성공적으로 변경되었습니다.')
        level1 = each_doc['level']
        exp1 = int(each_doc['exp']) + int(arg2)
        if exp1 >= multiply(level1, 350):
            level1 = int(level1) + 1
            exp1 = 0
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)
            ctx.send(f'{ctx.author.name}님이 {level1}레벨으로 레벨업 하였습니다!')
        else:
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)


@_expadd.error
async def expadderror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(administrator=True)
@Client.command(name='expset')
async def _expset(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='leveling')
    author = arg1.id
    author1 = arg1.name
    filter1 = {"_id":author}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":author, "name":author1, "exp":0, "level":1}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ctx.send('성공적으로 변경되었습니다.')
        level1 = each_doc['level']
        exp1 = int(arg2)
        if exp1 >= multiply(level1, 350):
            level1 = int(level1) + 1
            exp1 = 0
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)
            ctx.send(f'{ctx.author.name}님이 {level1}레벨으로 레벨업 하였습니다!')
        else:
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)


@_expset.error
async def expseterror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(administrator=True)
@Client.command(name='expdelete')
async def _expdelete(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='leveling')
    author = arg1.id
    author1 = arg1.name
    filter1 = {"_id":author}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":author, "name":author1, "exp":0, "level":1}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ctx.send('성공적으로 변경되었습니다.')
        level1 = each_doc['level']
        exp1 = int(each_doc['exp']) + int(arg2)
        if exp1 >= multiply(level1, 350):
            level1 = int(level1) + 1
            exp1 = 0
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)
            ctx.send(f'{ctx.author.name}님이 {level1}레벨으로 레벨업 하였습니다!')
        else:
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)


@_expdelete.error
async def expdeleteerror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(administrator=True)
@Client.command(name='leveladd')
async def _leveladd(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='leveling')
    author = arg1.id
    author1 = arg1.name
    filter1 = {"_id":author}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":author, "name":author1, "exp":0, "level":1}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ctx.send('성공적으로 변경되었습니다.')
        level1 = int(each_doc['level']) + int(arg2)
        exp1 = int(each_doc['exp'])
        if exp1 >= multiply(level1, 350):
            level1 = int(level1) + 1
            exp1 = 0
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)
            ctx.send(f'{ctx.author.name}님이 {level1}레벨으로 레벨업 하였습니다!')
        else:
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)


@_leveladd.error
async def leveladderror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(administrator=True)
@Client.command(name='레벨증가')
async def _레벨증가(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='leveling')
    author = arg1.id
    author1 = arg1.name
    filter1 = {"_id":author}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":author, "name":author1, "exp":0, "level":1}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ctx.send('성공적으로 변경되었습니다.')
        level1 = int(each_doc['level']) + int(arg2)
        exp1 = int(each_doc['exp'])
        if exp1 >= multiply(level1, 350):
            level1 = int(level1) + 1
            exp1 = 0
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)
            ctx.send(f'{ctx.author.name}님이 {level1}레벨으로 레벨업 하였습니다!')
        else:
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)


@_레벨증가.error
async def 레벨adderror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(administrator=True)
@Client.command(name='levelset')
async def _levelset(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='leveling')
    author = arg1.id
    author1 = arg1.name
    filter1 = {"_id":author}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":author, "name":author1, "exp":0, "level":1}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ctx.send('성공적으로 변경되었습니다.')
        level1 = int(arg2)
        exp1 = int(each_doc['exp'])
        if exp1 >= multiply(level1, 350):
            level1 = int(level1) + 1
            exp1 = 0
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)
            ctx.send(f'{ctx.author.name}님이 {level1}레벨으로 레벨업 하였습니다!')
        else:
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)


@_levelset.error
async def levelseterror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(administrator=True)
@Client.command(name='레벨설정')
async def _레벨설정(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='leveling')
    author = arg1.id
    author1 = arg1.name
    filter1 = {"_id":author}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":author, "name":author1, "exp":0, "level":1}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ctx.send('성공적으로 변경되었습니다.')
        level1 = int(arg2)
        exp1 = int(each_doc['exp'])
        if exp1 >= multiply(level1, 350):
            level1 = int(level1) + 1
            exp1 = 0
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)
            ctx.send(f'{ctx.author.name}님이 {level1}레벨으로 레벨업 하였습니다!')
        else:
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)


@_레벨설정.error
async def 레벨seterror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(administrator=True)
@Client.command(name='leveldelete')
async def _leveldelete(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='leveling')
    author = arg1.id
    author1 = arg1.name
    filter1 = {"_id":author}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":author, "name":author1, "exp":0, "level":1}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ctx.send('성공적으로 변경되었습니다.')
        level1 = int(each_doc['level']) - int(arg2)
        exp1 = int(each_doc['exp'])
        if exp1 >= multiply(level1, 350):
            level1 = int(level1) + 1
            exp1 = 0
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)
            ctx.send(f'{ctx.author.name}님이 {level1}레벨으로 레벨업 하였습니다!')
        else:
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)


@_leveldelete.error
async def 레벨deleteerror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(administrator=True)
@Client.command(name='레벨감소')
async def _레벨감소(ctx, arg1:discord.Member, arg2):
    client1 = pymongo.MongoClient(pymongotoken)
    clientdiscord = client1.get_database(name='discord')
    clientdictionary = clientdiscord.get_collection(name='leveling')
    author = arg1.id
    author1 = arg1.name
    filter1 = {"_id":author}
    if clientdictionary.find_one(filter=filter1) is None:
        memberdictionary = {"_id":author, "name":author1, "exp":0, "level":1}
        print(memberdictionary)
        clientdictionary.save(memberdictionary)
    cursor = clientdictionary.find(filter1)
    for each_doc in cursor:
        ctx.send('성공적으로 변경되었습니다.')
        level1 = int(each_doc['level']) - int(arg2)
        exp1 = int(each_doc['exp'])
        if exp1 >= multiply(level1, 350):
            level1 = int(level1) + 1
            exp1 = 0
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)
            ctx.send(f'{ctx.author.name}님이 {level1}레벨으로 레벨업 하였습니다!')
        else:
            filter2 = {"_id":each_doc['_id'], "name":each_doc['name'], "exp":exp1, "level":level1}
            clientdictionary.replace_one(filter=filter1, replacement=filter2)


@_레벨감소.error
async def leveldeleteerror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(administrator=True)
@Client.command(name='clear')
async def _clean(ctx, arg1):
    deleted = await ctx.message.channel.purge(limit=int(arg1))
    deletemessage = await ctx.send(f'{len(deleted)}개만큼 지웠습니다.')
    newdeletemessage = await ctx.fetch_message(deletemessage.id)


@_clean.error
async def cleanerror(ctx, error):
    print(error)
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

@has_permissions(administrator=True)
@Client.command(name='청소')
async def _청소(ctx, arg1):
    deleted = await ctx.message.channel.purge(limit=int(arg1))
    deletemessage = await ctx.send(f'{len(deleted)}개만큼 지웠습니다.')
    newdeletemessage = await ctx.fetch_message(deletemessage.id)


@_clean.error
async def cleanerror(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "미안하지만 {}님은 권한이 없습니다.".format(ctx.message.author)
        await ctx.send(text)

def todaycalculate():
    datetimetoday = datetime.datetime.today()
    today2 = str(datetimetoday.year) + '년 ' + str(datetimetoday.month) + '월 ' + str(datetimetoday.day) + '일 ' + str(datetimetoday.hour) + '시 ' + str(datetimetoday.minute) + '분 ' + str(datetimetoday.second) + '초 '
    return today2

def add(x, y):
    return int(x) + int(y)

def subtract(x, y):
    return int(x) - int(y)

def multiply(x, y):
    return int(x) * int(y)

def divide(x, y):
    return int(x) / int(y)

Client.run(TOKEN)