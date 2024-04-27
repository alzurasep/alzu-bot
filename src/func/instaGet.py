from instaloader import Instaloader, Profile

def instaGet( hesap ):
    
    loader = Instaloader()
    profile = Profile.from_username( loader.context, hesap )

    url = profile.profile_pic_url

    return url

def instaGetFollowers( hesap ):
    
    loader = Instaloader()
    profile = Profile.from_username( loader.context, hesap )



    return profile.followers


def instaGetFollowing( hesap ):
    
    loader = Instaloader()
    profile = Profile.from_username( loader.context, hesap )



    return profile.followees

def instaGetId( hesap ):
    
    loader = Instaloader()
    profile = Profile.from_username( loader.context, hesap )



    return profile.userid