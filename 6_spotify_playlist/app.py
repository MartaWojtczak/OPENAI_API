#libraries
import spotipy
from dotenv import dotenv_values
import openai
import json

config = dotenv_values(".env")
openai.api_key = config["API"]

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
playlist=get_playlist("energetic music for yoga practice in a sailing event in the morning", 3)

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
    name="TEST PLAYLIST"
)

#spotify add songs to playlist
added_songs=sp.user_playlist_add_tracks(
    current_user["id"], 
    created_playlist["id"], 
    tracks
)