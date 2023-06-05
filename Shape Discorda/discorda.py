import discord
import chatgpt

client = discord.Client(intents=discord.Intents.default())
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!chatgpt"):
        prompt = message.content[len("!chatgpt"):]
        response = chatgpt.generate_text(prompt)
        await message.channel.send(response)

client.run("MTExNTI2ODA2MTU2NjYwNzQzMQ.GomsMX.YMPqnj-qTYmGaH7w-909PtT-x747HI8xK1USbw")
