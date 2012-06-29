import twitter, argparse, sys, os
import config
from cobe.brain import Brain

parser = argparse.ArgumentParser(description="Post ebooks tweets to twitter.")
parser.add_argument('-o', '--stdout', action='store_true', help="Output to stdout instead of posting to twitter.")
parser.add_argument('-t', '--tweet', help="Tweet arbitrary text instead of using the brain.")

args = parser.parse_args()

api = twitter.Api(**config.api)

if args.tweet:
	api.PostUpdate(args.tweet)
else:

	b = Brain(os.path.join(os.path.dirname(__file__), 'cobe.brain'))

	#truncate to 140 characters, do not cut off words
	def smart_truncate(content, length=140):
	    if len(content) <= length:
	        return content
	    else:
	        return content[:length].rsplit(' ', 1)[0]

	# get a reply from brain, encode as UTF-8
	tweet = smart_truncate(b.reply("").encode('utf-8', 'replace'))

	if args.stdout:
		print tweet
	else:
		status = api.PostUpdate(tweet)
