#Lists credentials needed for various API projects

"""
Step 1: Register and Application at https://www.tumblr.com/oauth/apps
This will give you your client key and client secret

Step 2: Use that info to get oauth token and secret at
https://api.tumblr.com/console/calls/user/info

Step 3: Fill in the relevant information below
"""
import pytumblr

client_key=''
client_secret=''
oauth_token=''
oauth_secret=''

TUMBLR_CLIENT = pytumblr.TumblrRestClient(
        consumer_key,
        consumer_secret,
        oauth_token,
        oauth_secret
)
