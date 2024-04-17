import discord, random, os, sys
from discord.ext import commands
from dotenv import load_dotenv


# Load the environment variables
load_dotenv()

# Discord Learn Bot Token
TOKEN = os.getenv('BOT_TOKEN')

# Discord Learning Server Public Channel ID
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

# Define intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Create a bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

# Generate a random filepath
def filepath_generator():
  filepaths = {
    1: "video-files/Dependency Injection.mp4",
    2: "video-files/Object & JSON Serialization.mp4",
    3: "video-files/Server-Side vs Client-Side.mp4",
  }
  return filepaths[random.randint(1, 3)]

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    # Call the send_media function with the desired arguments
    await send_media(bot, CHANNEL_ID, filepath_generator())

async def send_media(ctx, channel_id: int, file_path: str):
    # Get the channel by its ID
    channel = bot.get_channel(channel_id)
    if channel is None:
        print(f"Channel ID not found.")

    # Send the media file
    with open(file_path, 'rb') as file:
        await channel.send(file=discord.File(file, filename=file_path))

    # Stop the bot after sending the media file and exit program
    await bot.close()
    sys.exit()

bot.run(TOKEN)
