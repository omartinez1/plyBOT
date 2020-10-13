import discord
# Import the os module.
import os
# Import load_dotenv function from dotenv module.
from discord.ext.commands import bot
from dotenv import load_dotenv
# Loads the .env file that resides on the same level as the script.
load_dotenv()
# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()


@client.event
async def on_message(message):
    # list commands
    if message.author == client.user:
        return
    if message.content.lower().startswith("!commands"):
        myEmbed = discord.Embed(title="HelpBot", description="Bot commands", color=0xD126BC)
        myEmbed.add_field(name="!emails", value="Gives TA & professors name & emails", inline=False)
        myEmbed.add_field(name="!exam", value="Exam info", inline=False)
        myEmbed.add_field(name="!topics", value="Topics discussed in latest q&a", inline=False)
        myEmbed.add_field(name="!curve", value="Curve for the class", inline=False)
        myEmbed.add_field(name="!testmistake", value="If you have a right answer on the test", inline=False)
        myEmbed.set_author(name="oscar's cool bot")
        myEmbed.add_field(name="!github", value="If you want to contribute to the bot.", inline=False)
        myEmbed.set_author(name="oscar's cool bot")
        await message.channel.send(embed=myEmbed)

    # produces results of commands
    if message.content.lower().startswith("!emails"):
        await message.channel.send("Professors and TA's emails:\nProfessor\nChinua Umoja\ncumoja1@gsu.edu\n"
                                   "TA\nShivam Jaitly\nsjaitly1@student.gsu.edu\nTA\nChan Aek"
                                   "Panichvatana: ncpanichvatana1@student.gsu.edu")
    if message.content.lower().startswith("!exam"):
        await message.channel.send("We only have 3 exams in the semester: 2 regular test and 1 final.")
    if message.content.lower().startswith("!curve"):
        await message.channel.send("Only if the class average is like less than a C low, don't count on it.")
    if message.content.lower().startswith("!topics"):
        await message.channel.send("Watch the Q&A. \n"
                                   "https://docs.google.com/document/d/1bVaHYG7Azg_3Lu1kQjpwZngRVaUOBBI008hdWY3jBpM/edit?usp=sharing")
    if message.content.lower().startswith("!testmistake"):
        await message.channel.send("Email the TA and CC the professor in the email.")


client.run('NzY1NjExOTI4OTE5MDgwOTgy.X4XVrA.rHrftNOte5Mce4TUd7n0PFYjqsY')
