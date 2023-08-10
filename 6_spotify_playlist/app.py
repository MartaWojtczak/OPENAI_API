#libraries
import spotipy
from dotenv import dotenv_values
import openai
import json
import argparse

#basic configuration
config = dotenv_values(".env")
openai.api_key = config["API"]

#parsing arguments feature
parser = argparse.ArgumentParser(description="Simple command line argument parser")
parser.add_argument("-p", type=str, required=True, help="The prompt to describe playlist")
parser.add_argument("-n", type=int, default=10, help="Number of songs in the playlist")
args = parser.parse_args()

#### get list of songs from openai model ####
#function
def get_playlist(prompt, count=10):
    example_json="""
    [
        {"song": "Hurt", "artist": "Johnny Cash"}, 
        {"song": "Someone Like You", "artist": "Adele"}, 
        {"song": "Yesterday", "artist": "The Beatles"}, 
        {"song": "Tears in Heaven", "artist": "Eric Clapton"}, 
        {"song": "Nothing Compares 2 U", "artist": "Sinead O'Connor"}
    ]
    """

    messages = [
    {"role": "system", "content": """
    You are helpful playlist generating assistant. 
    You should generate a list of songs and their artists according to a text prompt. 
    You should return a JSON array, where each element follows this format: 
    {"song": <song_title>, "artist": <artist_name>}. """},
    {"role": "user", "content": "Generate a playlist of 5 songs based on this prompt: sad songs"}, 
    {"role": "assistant", "content": example_json}, 
    {"role": "user", "content":f"""
    Generate a playlist of {count} songs based on this prompt: 
    {prompt}"""}
]

    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo"
        , messages=messages
        , max_tokens = 400
    )

    return json.loads(response["choices"][0]["message"]["content"])
#execute function - get playlist
playlist=get_playlist(args.p, args.n)

#### spotify part ####
#connect to spotify
sp=spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        client_id=config["SPOTIFY_CLIENT_ID"], 
        client_secret=config["SPOTIFY_CLIENT_SECRET"], 
        redirect_uri="http://localhost:9999", 
        scope="playlist-modify-private"
    )
)

current_user = sp.current_user()
assert current_user is not None

#spotify searching engine
tracks =[]
for i in playlist:
    artist, song = i["artist"], i["song"]
    query = f"{song} {artist}"
    search_results=sp.search(q=query, type="track", limit=1)
    tracks.append(search_results["tracks"]["items"][0]["id"])

#spotify create playlist
created_playlist=sp.user_playlist_create(
    current_user["id"], 
    public=False, 
    name=args.p
)

#spotify add songs to playlist
added_songs=sp.user_playlist_add_tracks(
    current_user["id"], 
    created_playlist["id"], 
    tracks
)