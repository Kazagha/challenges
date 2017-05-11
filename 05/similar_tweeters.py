import sys
import usertweets
import re
from collections import Counter

TOKEN = re.compile(r'\b\w{2}\w+')
VOID_WORDS = {'and','are','the','use','then','these','set','https','from','can','you','has','that','will','was'}

def _tokenize(tweets):

    tweet_text = ''.join(line for line in tweets).lower()

    # Remove digits, punctuation and works with less than three letters
    tweet_text = TOKEN.findall(tweet_text)

    # filtering out stop words, URLs, digits, punctuation,
    # words that only occur once or are less than 3 characters (and/or other noise ...)
    #print(Counter(tweet_text))

    # Remove words that occur only once
    return _remove_low_count(tweet_text)

def _remove_low_count(tweet):
    tweet_dict = Counter(tweet)
    return ({word for word in tweet_dict if tweet_dict[word] > 1} - VOID_WORDS)

def similar_tweeters(user1, user2):
    user1_tweets = usertweets.UserTweets(user1)
    #user2_tweets = usertweets.UserTweets(user2)

    t = _tokenize(t.text for t in user1_tweets)
    print(list(t))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
