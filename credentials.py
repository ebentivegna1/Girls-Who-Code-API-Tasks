#Lists credentials needed for various API projects

"""
Step 1: Register and Application at https://www.tumblr.com/oauth/apps
This will give you your client key and client secret

Step 2: Use that info to get oauth token and key at
https://api.tumblr.com/console/calls/user/info

Step 3: Fill in the relevant information below
"""
import pytumblr

consumer_key='FozOJDiIYSYsK23oyg1DNjkM7BgfA3MFehb9uOzv9wfcyFzE93'
consumer_secret='vyBqvg2hVWC2gCjPO59kSxikh8c2Iq8BHSeLL55lUguNvTJ11o'
oauth_token='UILvKnralDxvXckwC1WH2H8YXB6CK0kqtcGl8weoEsVjkSTe6i'
oauth_secret='DKLkma3Jh4fnHuNy8X9RC4z32cMn19mWjvknyPVuUbixdoTWBu'

TUMBLR_CLIENT = pytumblr.TumblrRestClient(
        consumer_key,
        consumer_secret,
        oauth_token,
        oauth_secret
)
