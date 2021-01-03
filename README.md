# SpotifyTopTracks
Spotify top 50 songs from 4 week, 6 month or 1 year plus
# Setup

the setup required for this program is incredibly simple and requires the following steps:
* Inputting of your token
  * can be pulled from spotify developer dashboard
* Time frame within top data method arguements
  * format {short_term: 4 weeks, medium_term: 6 months, long_term: 12 months +} 
  

# Upgrades to make
program in current form requires an OAuth2 token to be pulled manually from spotifys dashboard and these token will expire every hour. Therefore, automatic token pulling could be implemented in order to allow the program to run without any prior setup needed.
