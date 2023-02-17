import discord, random
from discord.ext import commands,tasks
from discord.commands import Option

class geral(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        
        self.bot = bot
    

    @discord.slash_command(name = "teste", description = "teste teste", guild_ids = [556910930395529237])
    async def teste(self, ctx):
        await ctx.respond("tes")

    '''@discord.slash_command(name="senha", description= "Senha necessária para se tornar um membro.")
    async def senha(self,ctx, senha:Option(str, "Digite a senha!", required = True), guild_ids = [556910930395529237]):
        senha = senha
        print(senha)
        if senha != self.Senha:
            await ctx.respond(f'Senha incorreta.', ephemeral= True)
            return
        role = discord.utils.get(ctx.guild.roles, name ="Membro")
        if role in ctx.user.roles:
            await ctx.respond(f'Você já é um membro!', ephemeral= True)
            return
        
        await ctx.respond(f'{ctx.author}', ephemeral= True)'''



def setup(bot:commands.Bot):
    bot.add_cog(geral(bot))