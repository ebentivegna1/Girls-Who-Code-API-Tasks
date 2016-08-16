#Edit credentials.py to include the Tumblr credentials for your blog
#See credentials.py for directions
from credentials import TUMBLR_CLIENT

#Edit this to be your blog name
blog_name="lainesw0rld"

#Create a quote post
def create_quote_post(text,speaker):
 	TUMBLR_CLIENT.create_quote(blog_name, quote=text, source=speaker)

#Create an audio post from soundcloud
def create_soundcloud(text,link):
 	TUMBLR_CLIENT.create_audio(blog_name,caption=text,external_url=link)

"""
 Can you figure out how to make a photo post
 Go to https://github.com/tumblr/pytumblr
 And see if you can add in a function that creates a photo post

 Extra credit: Write two functions:
 1) Creates a photo post from a file on your computer
 2) Creates a photo post from a link online
"""
