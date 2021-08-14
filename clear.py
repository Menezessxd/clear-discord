import discord
from discord.ext import commands

token   = "token"
prefixo = "prefix"

bot = commands.Bot(command_prefix=prefixo, self_bot=True)

@bot.command()
async def clear(ctx, limit: int=None):
   passed = 0
   failed = 0
   async for msg in ctx.message.channel.history(limit=limit):
       if msg.author.id == bot.user.id:
           try:
               await msg.delete()
               passed += 1
           except:
               failed += 1
   print(f" [Finalizado] {passed} Mensagens removidas e {failed} com erro.")

bot.run(token, bot=False)
