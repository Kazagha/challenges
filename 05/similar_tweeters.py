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

    # Remove stop words
    tweet_text = (word for word in tweet_text if word not in STOP_WORDS)

    # Use the Counter library to determine how many times each word occurs
    tweet_dict = Counter(tweet_text).most_common(10)

    # Remove words that occur only once
    # Remove any of the words in the STOP_WORD list
    return (word[0] for word in tweet_dict)

def _load_stop_words():
    with open('stop_words.txt') as words:
        return list(word.strip('\n') for word in words)

def similar_tweeters(user1, user2):
    STOP_WORDS = _load_stop_words()

    # Fetch User Tweets
    user1_tweets = usertweets.UserTweets(user1)
    user2_tweets = usertweets.UserTweets(user2)

    # Tokenize Tweets
    user1_tweets = list(_tokenize((t.text for t in user1_tweets), STOP_WORDS))
    user2_tweets = list(_tokenize((t.text for t in user2_tweets), STOP_WORDS))

    # Return words that are in both lists
    return (word_1 for word_1 in user1_tweets if word_1 in user2_tweets)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
