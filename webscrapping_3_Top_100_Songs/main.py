from pprint import pprint
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = "2000-03-04"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

data = response.text
soup = BeautifulSoup(data, "html.parser")

h3_tags = soup.find_all('h3', id="title-of-a-story")
h3_tags_text = [tag.getText() for tag in h3_tags]
count = 0
indices_of_writer=[]
for i in h3_tags_text:
    if i == '\n\n\t\n\t\n\t\t\n\t\t\t\t\tSongwriter(s):\t\t\n\t\n':
        indices_of_writer.append(count)
    count+=1

song_names = []
for i in indices_of_writer[1:]:
    namestring = h3_tags_text[i-1].split('\n\n\t\n\t\n\t\t\n\t\t\t\t\t')[1].split('\t\t\n\t\n')[0]
    song_names.append(namestring)


pprint(song_names)
print(len(song_names))

CLIENT_ID = 'f705c187325e41288c1e0c4c41479a34'
CLIENT_SECRET = 'bf649a4fbd6d4d73a883b138393589b7'

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = spotify.current_user()['id']

song_uris = []
year = date.split('-')[0]

for song in song_names:
    result = spotify.search(q=f'track:{song}', type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found in Spotify. SKIPPED .")

playlist = spotify.user_playlist_create(user=user_id, name = f"{date} 100 Trending Songs Today - by Billboard", public=False)
print(playlist)

spotify.playlist_add_items(playlist_id=playlist['id'], items=song_uris)