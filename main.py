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

@bot.slash_command(name="senha", description= "Senha necessária para se tornar um membro.")
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

@bot.slash_command(name = "inicio")
async def inicio(ctx):
    await ctx.send(file=discord.File("Recursos/Teste.png"))
    
    embed = discord.Embed(title = "【Ｂｅｍ　ｖｉｎｄｏ　ａｏ　Ｓｉｎｄｉｃａｔｏ！】", description ="Frase motivacional 1", color = discord.Color.gold())
    embed.add_field(name="Titulo 1", value="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras pretium sapien quis volutpat blandit. Nullam eu mattis urna. ")
    embed.add_field(name="Titulo 3", value="Quisque ac velit vitae massa suscipit condimentum. In vitae mattis libero. Donec blandit mi nec ornare fermentum.")
    embed.set_footer(text="Footer", icon_url= ctx.user.avatar)
    embed.set_image(url="https://i.imgur.com/5ZO3qC9.png")
    #embed.set_author(name=ctx.author.name, icon_url=ctx.user.avatar)
    await ctx.send(embed=embed)

    
bot.run(Key)