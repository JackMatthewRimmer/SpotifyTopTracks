'''
2 Changes needed;
imputting of your token within the token varible(exipres every hour),
time frame within the top data arguments to change which period the top songs are pulled from.

client_id and secret left empty if users wish to implement automated token pulling
'''

import requests
import json
from datetime import date
client_id = ""
client_secret = ""
token = "INSERT_YOUR_TOKEN_HERE"

class spotify_stats:

    def __init__(self, client_id, secret, token):
        self.client_id = client_id
        self.secret = secret
        self.token = token

    def user_id(self):
        query = "https://api.spotify.com/v1/me"
        header = {"Authorization": "Bearer {}".format(self.token)}
        r = requests.get(query, headers=header)
        return (r.json()['id'])

    def top_data(self, type, time_frame, limit):
        '''
        type = tracks/artists
        time_frame = (long/medium/short)_term, Years/6 Months/4 Weeks
        limit = limit of returned items
        '''
        query = "https://api.spotify.com/v1/me/top/{}".format(type)
        header = {"Authorization": "Bearer {}".format(self.token)}
        params = {"limit": limit,
                  "time_range": time_frame}
        r = requests.get(query, params=params, headers=header)
        return r.json()['items']

    def playlist_id(self):
        user_id = self.user_id()
        query = "https://api.spotify.com/v1/users/{}/playlists".format(user_id)
        params = {"limit": "50"}
        header = {"Authorization": "Bearer {}".format(self.token)}
        r = requests.get(query, headers=header, params=params)
        return r.json()['items'][0]['id']

    def add_songs(self):
        ids = [item['uri'] for item in self.top_data("tracks", "short_term", "100")]
        playlist_id = self.playlist_id()
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
        params = {"position": "0"}
        header = {"Authorization": "Bearer {}".format(self.token),
                  "Content-Type": "application/json"}
        request_body = json.dumps({"uris": ids})
        r = requests.post(query, params=params, data=request_body, headers=header)
        print(r.json())

    def create_playlist(self):
        user_id = self.user_id()
        time = str(date.today())
        query = "https://api.spotify.com/v1/users/{}/playlists".format(user_id)
        print(query)
        header = {"Authorization": "Bearer {}".format(self.token),
                  "Content-Type": "application/json"}
        request_body = json.dumps(
            {"name": "Your Top Songs {}".format(time),
             "public": True,
             "description": "this is your top 50 songs"})

        r = requests.post(query, data=request_body, headers=header)

    def check(self):
        playlist_id = self.playlist_id()
        query = "https://api.spotify.com/v1/playlists/{}".format(playlist_id)
        header = {"Authorization": "Bearer {}".format(self.token),
                  "Content-Type": "application/json"}
        r = requests.get(query, headers=header)
        return r.json()['name']


def main():
    time = str(date.today())
    obj = spotify_stats(client_id, client_secret, token)
    if obj.check() != "Your Top Songs {}".format(time):
        obj.create_playlist()
        obj.add_songs()
    else:
        obj.add_songs()

if __name__ == '__main__':
    main()
