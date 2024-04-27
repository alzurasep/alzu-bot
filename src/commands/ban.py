from nextcord.ext.commands import Cog
from nextcord.ext import application_checks
from nextcord import slash_command, Interaction, Embed, User



class ban( Cog ):
    
    @slash_command( name = 'ban', description = 'Kullanıcıyı sunucudan yasaklar.')
    @application_checks.has_permissions( ban_members = True )
    async def ban( self, interaction: Interaction, hesap : User, sebep : str = None ):
        if sebep:
            sebep = f"{ sebep }, { interaction.user }"
        else:
            sebep = f"Sebep Verilmedi, { interaction.user }"

        async for i in interaction.guild.bans():
            if hesap.id == i.user.id:
                Mesaj = Embed( title = f"'{ hesap }' Halihazırda yasaklı.")
                Mesaj.add_field( name = 'Yasaklanma Sebebi:', value = i.reason )
                Mesaj.set_thumbnail( url = hesap.avatar.url)

                await interaction.response.send_message( embed = Mesaj )
                break
        else:
            Mesaj = Embed( title = f"'{ hesap }' Başarıyla yasaklandı." )
            Mesaj.add_field( name = 'Admin:', value = interaction.user )
            Mesaj.add_field( name = 'Mahkum:', value = hesap )
            Mesaj.set_thumbnail( url = hesap.avatar.url)

            await interaction.guild.ban( hesap, reason = sebep )
            await interaction.response.send_message( embed = Mesaj )



    @slash_command( name = 'unban', description = 'Kullanıcının yasağını kaldırır.' )
    @application_checks.has_permissions( ban_members = True )
    async def unban( self, interaction: Interaction, hesap : User, sebep : str = None ):
        if sebep:
            sebep = f"{ sebep }, { interaction.user }"
        else:
            sebep = f"Sebep Verilmedi, { interaction.user }"

        async for i in interaction.guild.bans():
            if hesap.id == i.user.id:
                Mesaj = Embed( title = f"'{ hesap }' Başarıyla yasağı kaldırıldı." )
                Mesaj.add_field( name = 'Admin:', value = interaction.user )
                Mesaj.add_field( name = 'Mahkum:', value = hesap )
                Mesaj.set_thumbnail( url = hesap.avatar.url)

                await interaction.guild.unban( hesap, reason = sebep )
                await interaction.response.send_message( embed = Mesaj )
                break
        else:
            Mesaj = Embed( title = f"'{ hesap }' Halihazırda yasaklı değil.")
            Mesaj.set_thumbnail( url = hesap.avatar.url)

            await interaction.response.send_message( embed = Mesaj )

def setup( client ): client.add_cog( ban( client ) )