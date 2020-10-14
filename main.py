import discord
from discord.ext import commands
import os
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv

# Credentials
load_dotenv('.env')

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
        myEmbed.add_field(name="!curve", value="Explains curve question.", inline=False)
        myEmbed.add_field(name="!testmistake", value="If you have a right answer on the test", inline=False)
        myEmbed.set_author(name="oscar's cool bot")
        myEmbed.add_field(name="!github", value="If you want to contribute to the bot.", inline=False)
        myEmbed.set_author(name="plc bot")
        await message.channel.send(embed=myEmbed)

    # produces results of commands
    if message.content.lower().startswith("!emails"):
        await message.channel.send("Professors and TA's emails:\nProfessor\nChinua Umoja\ncumoja1@gsu.edu\n"
                                   "TA\nShivam Jaitly\nsjaitly1@student.gsu.edu\nTA\nChan Aek"
                                   "Panichvatana: ncpanichvatana1@student.gsu.edu")
    if message.content.lower().startswith("!exam"):
        await message.channel.send("We only have 3 exams in the semester: 2 regular tests and 1 final.")
    if message.content.lower().startswith("!curve"):
        await message.channel.send("Only if the class average is like less than a C-, don't count on it.")
    if message.content.lower().startswith("!topics"):
        await message.channel.send("Watch the Q&A, please: \n"
                                   "https://docs.google.com/document/d/1bVaHYG7Azg_3Lu1kQjpwZngRVaUOBBI008hdWY3jBpM/edit?usp=sharing")
    if message.content.lower().startswith("!testmistake"):
        await message.channel.send("Email a TA and CC the professor in the email.")
    if message.content.lower().startswith("!github"):
        await message.channel.send("Feel free to contribute:\nhttps://github.com/omartinez1/plyBOT")


client.run(os.getenv('TUTORIAL_BOT_TOKEN'))
