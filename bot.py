import hikari
from hikari import PermissionOverwrite, PermissionOverwriteType, Permissions, snowflakes
import lightbulb

token = "bot token here"
guild_id = guild id here
welcome_id = channel id here

bot = lightbulb.BotApp(
    token=token, default_enabled_guilds=(guild_id), intents=hikari.Intents.ALL
)

@bot.listen(hikari.events.MemberCreateEvent)
async def userjoined(event: hikari.events.MemberCreateEvent):
    join = hikari.Embed(
        title=f"👋  Hello {event.member.username}!",
        description="Welcome to {}!".format(event.get_guild().name),
        color=(0, 255, 0),
    )
    join.set_thumbnail(event.member.avatar_url)
    await bot.rest.create_message(channel=welcome_id, content=join)

@bot.listen(hikari.events.MemberDeleteEvent)
async def userleft(event: hikari.events.MemberDeleteEvent):
    leave = hikari.Embed(
        title="😢  Goodbye {}!".format(event.user.username),
        description="User {} left {}".format(
            event.user.username, event.get_guild().name
        ),
        color=(255, 0, 0),
    )
    leave.set_thumbnail(event.user.avatar_url)
    await bot.rest.create_message(channel=welcome_id, content=leave)


bot.run(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(
        name="You join this server!",
        type=hikari.ActivityType.WATCHING,
    ),
)
