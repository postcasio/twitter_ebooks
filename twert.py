import twitter
#get keys/secrets from dev.twitter.com signed in as the bot account
api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='')

from cobe.brain import Brain

b = Brain("cobe.brain")

#truncate to 140 characters, do not cut off words
def smart_truncate(content, length=140):
    if len(content) <= length:
        return content
    else:
        return content[:length].rsplit(' ', 1)[0]

#feed cobe an empty reply so it babbles
status = api.PostUpdate((smart_truncate(b.reply(""))))
