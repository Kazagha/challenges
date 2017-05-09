import sys
import usertweets
import re

TOKEN = re.compile(r'\b\w{2}\w+')

def _tokenize(tweets):

    tweet_text = ''.join(line for line in tweets)

    print(TOKEN.findall(tweet_text))

    # filtering out stop words, URLs, digits, punctuation, words that only occur once or are less than 3 characters (and/or other noise ...)

    # Remove Punctuation, digits

    pass

def similar_tweeters(user1, user2):
    user1_tweets = usertweets.UserTweets(user1)
    user2_tweets = usertweets.UserTweets(user2)

    t = _tokenize(t.text for t in user1_tweets)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
