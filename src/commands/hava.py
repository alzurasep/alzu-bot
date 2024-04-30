from os import getenv
from nextcord.ext.commands import Cog 
from nextcord import slash_command, Interaction, Embed
from dotenv import load_dotenv
from http import client
from json import loads
from nextcord.ui import Button, View, button
from nextcord import ButtonStyle
load_dotenv('/.env')


Connection = client.HTTPSConnection( "api.collectapi.com" )
        
headers = {
            'content-type': "application/json",
            'authorization': getenv( 'collectToken' )
        }





        
class hava( Cog ):
    def __init__( self, client ):
        self.client = client

    
    @slash_command( name = "hava", description = "Secilen Sehrin Hava Durumu" )
    async def hava( self, interaction : Interaction, sehir ):
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
        
        Mesaj = Embed( title = f"{ Tarih } Tarihli { sehir.capitalize() } Hava Durumu")
        Mesaj.set_thumbnail( url = Icon )
        Mesaj.add_field( name = "Derece", value = Derece )
        Mesaj.add_field( name = "Nem", value = Nem )
        

        sonrakiTarih = Button( label = "Sonraki Tarih", style = ButtonStyle.green )


        async def sonrakiTarih_callback( self ):
    
            Connection.request( 'GET', f'/weather/getWeather?data.lang=tr&data.city={ sehir }', headers = headers )
        
            Response = Connection.getresponse()
        
            Data = Response.read()
            Data = Data.decode( 'utf-8' )  
        
        
            Sonuc = loads( Data )
            Sonuc = Sonuc[ 'result' ][ 1 ]
            Tarih = Sonuc[ 'date' ]
            Derece = Sonuc[ 'degree' ]
            Nem = Sonuc[ 'humidity' ]
            Icon = Sonuc[ 'icon' ]
        
            Mesaj = Embed( title = f"{ Tarih } Tarihli { sehir.capitalize() } Hava Durumu")
            Mesaj.set_thumbnail( url = Icon )
            Mesaj.add_field( name = "Derece", value = Derece )
            Mesaj.add_field( name = "Nem", value = Nem )
            await interaction.edit_original_message( embed = Mesaj, view = None )
      

        
        sonrakiTarih.callback = sonrakiTarih_callback
        view = View( timeout = 190)
        view.add_item( sonrakiTarih )
        await interaction.response.send_message( embed = Mesaj, view = view )    
        
        
            

def setup( client ): client.add_cog( hava( client ))
