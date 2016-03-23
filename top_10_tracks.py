#Simple use case of Spotify API
#Go to Spotify, look up an artist and click on the three dots button next to the following button for that artist
#Once you click on that button grab the "Spotify URI" for that artist
#THe Spotify URI will be what you input as the artist_key in the function

import spotipy

spotify = spotipy.Spotify()

def top_ten_tracks(artist_name, artist_key):
	results = spotify.artist_top_tracks(artist_key)

	print "Top 10 Tracks For:  " + artist_name
	for track in results['tracks'][:10]:
		print 'track  : ' + track['name']
