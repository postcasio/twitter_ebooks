import twitter, os
import config
from simplejson import loads, dumps
from cobe.brain import Brain

b = Brain(os.path.join(os.path.dirname(__file__), 'cobe.brain'))

try:
	state = loads(open(os.path.join(os.path.dirname(__file__), '.state'), 'r').read())
except:
	state = {}

if 'accounts' not in state:
	state['accounts'] = {}
if 'last_reply' not in state:
	state['last_reply'] = 0

api = twitter.Api(**config.api)

b.start_batch_learning()

tweets = 0

def smart_truncate(content, length=140):
	    if len(content) <= length:
	        return content
	    else:
	        return content[:length].rsplit(' ', 1)[0]

for account in config.dump_accounts:
	print "Grabbing tweets for %s" % account
	
	if account in state['accounts']:
		last_tweet = long(state['accounts'][account])
	else:
		last_tweet = 0

	try:
		timeline = api.GetUserTimeline(
			account, count=200, since_id=last_tweet,
	
			include_rts=not config.skip_retweets,
			exclude_replies=config.skip_replies,
	
			trim_user=True,
			include_entities=False
		)
	except:
		continue

	for tweet in timeline:
		b.learn(tweet.text)
		last_tweet = max(tweet.id, last_tweet)
		tweets += 1

	print "%d found..." % tweets
	state['accounts'][account] = str(last_tweet)

print "Learning %d tweets" % tweets
b.stop_batch_learning()

if config.replies:
	print "Performing replies"
	
	last_tweet = long(state['last_reply'])

	replies = api.GetReplies(since_id=last_tweet)

	for reply in replies:
		try:
			api.PostUpdate(smart_truncate('@%s %s' % (reply.user.screen_name, b.reply(reply.text).encode('utf-8', 'replace'))), in_reply_to_status_id=reply.id)
		except:
			print 'Error posting reply.'
		last_tweet = max(reply.id, last_tweet)

	state['last_reply'] = str(last_tweet)

print "Saving state"

open(os.path.join(os.path.dirname(__file__), '.state'), 'w').write(dumps(state))
