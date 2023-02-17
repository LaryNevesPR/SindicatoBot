import discord, os, random
#from discord.commands import Option
from discord.ext import commands, tasks
from discord.commands import Option
from key import Key
from datetime import datetime


intents = discord.Intents().all()
bot = commands.Bot(intents=intents)

Senha = 6969

for filename in os.listdir("./Comandos"):
    if filename.endswith(".py") and not filename.startswith("__"):
        bot.load_extension("Comandos.{0}".format(filename[:-3]))

@bot.event
async def on_ready():
    print("I'm ready to go!")
    printer.start()


@tasks.loop(seconds= 10)
async def printer():
    channel = bot.get_channel(723623863057121281)
    global Senha
    Senha = random.randint(10_000,99_999)
    print(Senha)
    #await channel.edit(name=f"Senha: {Senha}")
    #await channel.send(Senha)

@bot.slash_command(name="verificar_senha", description="Somente admins.")
async def verfsenha(ctx):
    await ctx.respond(f'Senha: {Senha}', ephemeral= True)

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
    
    #await ctx.respond(f'{ctx.author}', ephemeral= True)'''

@bot.slash_command(name = "inicio")
async def inicio(ctx):
    await ctx.send(file=discord.File("Recursos/Teste.png"))
    await ctx.send(":star:【Ｂｅｍ　ｖｉｎｄｏ　ａｏ　Ｓｉｎｄｉｃａｔｏ！】:star:")
    await ctx.send("================================= /=/        /=/ =================================")
    await ctx.send(":coin: Não acredite em tudo, principalmente na 'verdade' ")
    await ctx.send(":coin: **Sindicato** aceita somente pessoas que podem trazer algum tipo conhecimento ou entreterimento para os demais membros. Sinta-se honrado ao ser convidado para ingressar.")
    await ctx.send(":coin: Para ter acesso ao servidor você precisa fornecer a **senha**, que diariamente é trocada.")
    await ctx.send(":coin: Caso tenha a senha, utilize o comando `/senha` e digite-a corretamente.")
    await ctx.send("================================= /=/ Regras /=/ =================================")
    await ctx.send("𝟷º Leia as regras!")
    await ctx.send("𝟸º Respeite todos os membros do servidor. Se você não conhece o membro não tente fazer brincadeiras com o mesmo. Lembre-se você provalmente é um **ningêm** para a maioria dos outros membros quando entrar no servidor.")
    await ctx.send("*Obs: caso precise de ajuda mande mensagem para um dos* <@&1075294781586026566>")
    await ctx.send("𝟹º Mande mensagens em seus respectivos canais! Bots no canal de Bots, assuntos específicos em canais do mesmo.")
    embed = discord.Embed(title = "【Ｌｅｍｂｒｅ－ｓｅ】", description ="Não acredite em tudo, principalmente na 'verdade'.", color = discord.Color.gold())
    embed.add_field(name="Seja Feliz", value="Sorria e acene.")
    embed.add_field(name="Aceite", value="Seja sindicalizado.")
    embed.set_footer(text="Footer", icon_url= "https://image.noelshack.com/fichiers/2017/41/3/1507739509-emote-blitz-does-not-compute.png")
    embed.set_image(url="https://i.imgur.com/5ZO3qC9.png")
    #embed.set_author(name=ctx.author.name, icon_url=ctx.user.avatar)
    await ctx.send(embed=embed)


bot.run(Key)