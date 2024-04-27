from nextcord.ext.commands import Cog 
from nextcord import slash_command, Interaction, Embed, SlashOption, PermissionOverwrite
from nextcord.ext import application_checks


class kanal( Cog ):
    
    @slash_command( name = 'kanal_yarat', description = 'Seçilen kategoriyle kanal yaratır.' )
    @application_checks.has_permissions( manage_channels = True )
    async def kanal_yarat( self, interaction: Interaction, kanal_ismi, kategori = SlashOption( name = 'kategori', description = 'Kategori', choices = [ 'yazi', 'ses' ], required = True ), ozel_kanal = SlashOption( name = 'ozel_kanal', description = 'Özel Kanal', choices = [ 'evet', 'hayir' ], required = False ) ):


        try:
            embed= Embed(title=f"{kanal_ismi} adinda kanal olusturuldu" )
            embed.add_field( name = 'Tarafından: ', value = interaction.user )
            embed.add_field( name = "Tip:", value = kategori )
            embed.add_field(name = "Kanal İsmi:", value = kanal_ismi )
            embed.set_image( url = interaction.user.avatar )
            if ozel_kanal == "evet":
                overwrites = {
                interaction.guild.default_role: PermissionOverwrite( read_messages = False ),
                interaction.guild.me: PermissionOverwrite( read_messages = True )
            }
                if kategori == "ses":
                    overwrites = {
                        interaction.guild.default_role: PermissionOverwrite( connect = False ),
                        interaction.guild.me: PermissionOverwrite( connect = True )
                    }
                    await interaction.guild.create_voice_channel( name = kanal_ismi, overwrites = overwrites )
                    await interaction.response.send_message( embed = embed )    
                else: 
                    overwrites = {
                        interaction.guild.default_role: PermissionOverwrite( read_messages = False ),
                        interaction.guild.me: PermissionOverwrite( read_messages = True )
                    }
                    await interaction.guild.create_text_channel( name = kanal_ismi, overwrites = overwrites )
                    await interaction.response.send_message( embed = embed )

            else:
                if kategori == "ses":
                    await interaction.guild.create_voice_channel( name = kanal_ismi )
                    await interaction.response.send_message( embed = embed )
                else:
                    await interaction.guild.create_text_channel( name = kanal_ismi )
                    await interaction.response.send_message( embed = embed )
                    
                

        except:
            pass



def setup( client ): client.add_cog( kanal( client ) )