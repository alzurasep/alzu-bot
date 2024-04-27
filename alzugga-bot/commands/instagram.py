from nextcord.ext.commands import Cog 
from nextcord import slash_command, Interaction, Embed 
from nextcord.ext import commands
import nextcord

from func.instaGet import instaGet, instaGetFollowers, instaGetFollowing, instaGetId

class instagram( Cog ):
    @commands.command( name = 'instagram', description = 'Girdiğiniz Instagram hesabının avatarını gösterir.' )
    async def instagram( self, interaction: nextcord.Message, hesap ):
        
        Mesaj = Embed( title = f"{ hesap } Adlı Instagram hesabının avatarı" )
        Mesaj.set_image( url = instaGet( hesap ) )
        Mesaj.add_field( name = 'Takipçi Sayısı:', value = instaGetFollowers( hesap ) )
        Mesaj.add_field( name = 'Takip Ediliyor:', value = instaGetFollowing( hesap ) )
        Mesaj.add_field( name = 'Hesap id:', value =instaGetId( hesap ) )
        
        await interaction.channel.send( embed = Mesaj )


    

def setup( client ): client.add_cog( instagram( client) )