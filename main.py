import discord
#from discord.commands import Option
from discord.ext import commands
from discord.commands import Option
from key import Key

intents = discord.Intents().all()
bot = commands.Bot(intents=intents)

Senha = "paz é um conto de fadas"

@bot.event
async def on_ready():
    print("I'm ready to go!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1075182206231785624)
    role = discord.utils.get(member.guild.roles, name ="Membro")
    await member.add_roles(role)
    guild = member.guild
    await channel.edit(name=f"Membros: {guild.member_count}")

@bot.slash_command(name="senha")
async def senha(ctx, senha:Option(str, "Digite a senha!", required = True)):
    senha = senha.lower()
    print(senha)
    if senha != Senha:
        await ctx.respond(f'Senha incorreta.', ephemeral= True)
        return
    role = discord.utils.get(ctx.guild.roles, name ="Membro")
    if role in ctx.user.roles:
        await ctx.respond(f'Você já é um membro!', ephemeral= True)
        return
    
    await ctx.respond(f'{ctx.author}', ephemeral= True)

bot.run(Key)