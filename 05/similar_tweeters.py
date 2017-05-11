import sys
import usertweets
import re
from collections import Counter

TOKEN = re.compile(r'\b\w{2}\w+')

def _tokenize(tweets, STOP_WORDS):

    # Collect the text into one string
    tweet_text = ''.join(line for line in tweets).lower()

    # Remove digits, punctuation and works with less than three letters
    tweet_text = TOKEN.findall(tweet_text)

    # Use the Counter library to determine how many times each word occurs
    tweet_dict = Counter(tweet_text)

    # Remove words that occur only once
    # Remove any of the words in the STOP_WORD list
    return {word for word in tweet_dict if tweet_dict[word] > 1}  - STOP_WORDS

def _load_stop_words():
    with open('stop_words.txt') as words:
        return {word.strip('\n') for word in words}

def similar_tweeters(user1, user2):
    STOP_WORDS = _load_stop_words()

    # Fetch User Tweets
    user1_tweets = usertweets.UserTweets(user1)
    #user2_tweets = usertweets.UserTweets(user2)

    # Tokenize Tweets
    user1_tweets = _tokenize((t.text for t in user1_tweets), STOP_WORDS)

    print(user1_tweets)

    print(f'Word List Length {len(t)}')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
