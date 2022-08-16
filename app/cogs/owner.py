import sys

import aiohttp
import discord
from app import typings
from discord.ext import commands


class Owner(commands.Cog):

  def __init__(self, bot: typings.ExtBotType) -> None:
    self.bot = bot

  @commands.command()
  @commands.is_owner()
  async def shutdown(self, ctx: discord.ApplicationContext) -> None:
    await ctx.send(":wave: Bye-bye!")
    await self.bot.close()

    self.bot.clear()
    sys.exit(0)

  @commands.command()
  @commands.is_owner()
  async def avatar(self, ctx: discord.ApplicationContext, url: discord.Option(str, "Enter new avatar link.")) -> None:
    async with aiohttp.ClientSession() as session:
      async with session.get(''.join(url)) as img:
        await self.bot.user.edit(avatar=await img.read())
    
    if self.bot.user.avatar.url is None:
      return

    await ctx.send(f":relaxed: I've a new avatar!\n{self.bot.user.avatar.url}")

  @commands.command()
  @commands.is_owner()
  async def username(self, ctx: discord.ApplicationContext, username: discord.Option(str, "Enter new username.")) -> None:
    await self.bot.user.edit(username=username)
    await ctx.send(f":relaxed: I've a new username! {self.bot.user}")


def setup(bot: typings.ExtBotType) -> None:
  bot.add_cog(Owner(bot))