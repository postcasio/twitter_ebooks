import twitter, os
import config
from simplejson import loads, dumps
from cobe.brain import Brain

b = Brain(os.path.join(os.path.dirname(__file__), 'cobe.brain'))

try:
	state = loads(open(os.path.join(os.path.dirname(__file__), '.state'), 'r').read())
except:
	state = {'accounts': {}}

api = twitter.Api(**config.api)

b.start_batch_learning()
tweets = 0
for account in config.dump_accounts:
	print "Grabbing tweets for %s" % account
	if account in state['accounts']:
		last_tweet = state['accounts'][account]
	else:
		last_tweet = 0
	latest_tweet = last_tweet
	timeline = api.GetUserTimeline(
		account, count=200, since_id=latest_tweet,

		include_rts=not config.skip_retweets,
		exclude_replies=config.skip_replies,

		trim_user=True,
		include_entities=False
	)

	for tweet in timeline:
		if tweet.id > last_tweet:
			b.learn(tweet.text)
			if tweet.id > latest_tweet:
				latest_tweet = tweet.id
			tweets += 1
	print "%d found..." % tweets
	state['accounts'][account] = latest_tweet

print "Learning %d tweets" % tweets
b.stop_batch_learning()
print "Saving data"

open(os.path.join(os.path.dirname(__file__), '.state'), 'w').write(dumps(state))
