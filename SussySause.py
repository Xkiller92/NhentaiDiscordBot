from discord.ext import commands
from NhentaiAPI import Doujin

TOKEN = "ODg3MDEwNjc1MDgyMjg1MDc3.YT97EA.MJeEuoSpMKoS6zQqSMD0ahC4I8k"

bot = commands.Bot(command_prefix='>')

@bot.command()
async def cover(ctx, num):
    doujin = Doujin(num)
    await ctx.send(doujin.get_page_by_number(1))
 
@bot.command()   
async def tags(ctx, num):
    doujin = Doujin(num)
    await ctx.send("tags\n" + doujin.get_tags())
    
@bot.command()    
async def info(ctx, num):
    doujin = Doujin(num)
    await ctx.send("Name: {}\nArtist: {}\nLanguages: {}\nPages:{}".format(
                                        doujin.get_name(),
                                        doujin.get_artist(),
                                        doujin.get_languages(),
                                        doujin.get_page_count()))

@bot.command()    
async def pages(ctx, num): 
    doujin = Doujin(num)
    
    for page in range(doujin.get_page_count()):
        await ctx.send(doujin.get_page_by_number(page + 1))
         
#@bot.command()
#async def command_list(ctx,):
    #for key in bot.all_commands:
        #await ctx.send(">" + key)



bot.run(TOKEN)