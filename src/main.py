from nextcord.ext import commands 
from nextcord import Intents
from dotenv import load_dotenv
from os import getenv, listdir

load_dotenv()

client = commands.Bot( command_prefix = ">>", intents = Intents.all() )

@client.event
async def on_ready():
    print( f'{ client.user } Aktif!' )
    
    

for i in listdir( 'commands' ):
    if i.endswith( '.py' ):
        client.load_extension( f'commands.{i[:-3]}' )



if __name__ == '__main__':
    token = getenv( 'token' )
    client.run( token )
    