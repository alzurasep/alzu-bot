import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv('/.env')


def getToken():
    SpotifyClientID = getenv( 'SpotifyClientID' )
    SpotifyClientSECRET = getenv( 'SpotifyClientSECRET' )

    head = { 'Content-Type': "application/x-www-form-urlencoded" }

    tokenGet = requests.post( "https://accounts.spotify.com/api/token", data = f"grant_type=client_credentials&client_id={ SpotifyClientID }&client_secret={ SpotifyClientSECRET }", headers = head )
    
    jsonTOKEN = tokenGet.json()
    accessTOKEN = jsonTOKEN[ 'access_token' ]
    
    return accessTOKEN

AUTH = { "Authorization": f"Bearer { getToken() }" }

def getSpotifyUrl( hesap ):
    
    API = requests.get( f"https://api.spotify.com/v1/users/{ hesap }", headers = AUTH )
    APIjson = API.json()
    APIimages = APIjson[ "images" ][ 1 ]
    APIurl = APIimages[ 'url' ]


    return APIurl

def getDisplayName( hesap ):

    API = requests.get( f"https://api.spotify.com/v1/users/{ hesap }", headers = AUTH )
    APIjson = API.json()
    APIname = APIjson[ 'display_name' ]

    return APIname

def getFollowersCount( hesap ):

    API = requests.get( f"https://api.spotify.com/v1/users/{ hesap }", headers = AUTH )
    APIjson = API.json()
    APICount = APIjson[ 'followers' ][ 'total' ]
    
    return APICount


def getPlaylists(hesap):
    API = requests.get( f"https://api.spotify.com/v1/users/{ hesap }/playlists", headers = AUTH )
    APIjson = API.json()
    return APIjson[ 'items' ]

