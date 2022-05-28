<h1 align="center">ActivityDiscord</h1>

<h1>Discord activities on nextcord (d.py fork).</h1> 


### pip install git+link :)


```Python
import nextcord
from nextcord.ext import commands
from DiscordActivity import Activity

bot = commands.Bot(command_prefix="!")
activities = Activity(bot=bot)

@bot.command()
async def fishing(ctx, voice: nextcord.VoiceChannel, name: str):
    activity = await activities.send_activity(name=name, voice=voice)
    await ctx.reply(f"Go fishing!\nhttps://discord.gg/{activity['code']}")

bot.run("your-bot-token")
```
