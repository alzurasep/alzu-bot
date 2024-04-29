from os import getenv
from nextcord.ext.commands import Cog 
from nextcord import slash_command, Interaction, Embed
from dotenv import load_dotenv
from http import client
from json import loads
from nextcord.ui import Button, View
from nextcord import ButtonStyle
load_dotenv('/.env')

class hava( Cog ):
    def __init__( self, client ):
        self.client = client

    
    @slash_command( name = "hava", description = "Secilen Sehrin Hava Durumu" )
    async def hava( self, interaction : Interaction, sehir ):
        Connection = client.HTTPSConnection( "api.collectapi.com" )
        
        headers = {
            'content-type': "application/json",
            'authorization': getenv( 'collectToken' )
        }
        
        Connection.request( 'GET', f'/weather/getWeather?data.lang=tr&data.city={ sehir }', headers = headers )
        
        Response = Connection.getresponse()
        
        Data = Response.read()
        Data = Data.decode( 'utf-8' )        

        Sonuc = loads( Data )
        Sonuc = Sonuc[ 'result' ][ 0 ]
        Tarih = Sonuc[ 'date' ]
        Derece = Sonuc[ 'degree' ]
        Nem = Sonuc[ 'humidity' ]
        Icon = Sonuc[ 'icon' ]
        

        Mesaj = Embed( title = f"{ sehir.capitalize() }, { Tarih } tarihli hava durumu" )
        Mesaj.set_thumbnail( url = Icon )
        Mesaj.add_field( name = 'Derece:', value = Derece )
        Mesaj.add_field( name = 'Nem:', value = Nem )
        

        
        sonrakiTarih = Button( label = "Sonraki Tarih", style = ButtonStyle.blurple )
        
        async def sonrakiTarih_callback( interaction : Interaction ):
            Sonuc = loads( Data )
            Sonuc = Sonuc[ 'result' ][ 1 ]
            Tarih = Sonuc[ 'date' ]
            Derece = Sonuc[ 'degree' ]
            Nem = Sonuc[ 'humidity' ]
            Icon = Sonuc[ 'icon' ]
        

            Mesaj = Embed( title = f"{ sehir.capitalize() }, { Tarih } tarihli hava durumu" )
            Mesaj.set_thumbnail( url = Icon )
            Mesaj.add_field( name = 'Derece:', value = Derece )
            Mesaj.add_field( name = 'Nem:', value = Nem )
            await interaction.message.edit( embed = Mesaj )
            
        sonrakiTarih.callback = sonrakiTarih_callback
        my_view = View( timeout = 60 )
        my_view.add_item( sonrakiTarih )

        await interaction.channel.send( embed = Mesaj, view = my_view )

def setup( client ): client.add_cog( hava( client ))