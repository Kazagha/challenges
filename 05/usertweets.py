from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', 'id_str created_at text')

class UserTweets(object):

    def __init__(self, handle, max_id=None):
        """Get handle and optional max_id.
        Use tweepy.OAuthHandler, set_access_token and tweepy.API
        to create api interface.
        Use _get_tweets() helper to get a list of tweets.
        Save the tweets as data/<handle>.csv"""
        # ...

        # Setup OAuth for the Tweepy API
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth)

        self.handle = handle
        self.max_id = max_id
        #self.output_file = f'{os.path.dirname(os.path.realpath(__file__))}\\{DEST_DIR}\\tweets.{EXT}'

        out_dir = os.path.join(DEST_DIR,self.handle)
        self.output_file = f'{out_dir}.{EXT}'

        self._tweets = list(self._get_tweets())

        #self._tweets = list(self._get_tweets())
        #self._save_tweets()

    def _get_tweets(self):
        """Hint: use the user_timeline() method on the api you defined in init.
        See tweepy API reference: http://docs.tweepy.org/en/v3.5.0/api.html
        Use a list comprehension / generator to filter out fields
        id_str created_at text (optionally use namedtuple)"""

        user_tweets = self.api.user_timeline(self.handle, max_id=self.max_id, count=NUM_TWEETS)
        for tweet in user_tweets:
            yield Tweet(tweet.id_str, tweet.created_at, tweet.text.replace('\n',''))

    def _save_tweets(self):
        """Use the csv module (csv.writer) to write out the tweets.
        If you use a namedtuple get the column names with Tweet._fields.
        Otherwise define them as: id_str created_at text
        You can use writerow for the header, writerows for the rows"""

        with open(f'{self.output_file}','w', newline='', encoding='utf8') as csvfile:

            fieldnames = Tweet._fields
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for tweet in self._get_tweets():
                writer.writerow({'id_str':tweet.id_str,'created_at':tweet.created_at,'text':tweet.text})

            #writer.writerow(Tweet._fields)
            #writer.writerows(self._tweets)

    def __len__(self):
        """See http://pybit.es/python-data-model.html"""
        return len(self._get_tweets())

    def __getitem__(self, pos):
        """See http://pybit.es/python-data-model.html"""
        return self._tweets[pos]

if __name__ == "__main__":

    user_tweets = UserTweets('pybites', '819831370113351680')
    user_tweets._save_tweets()

    #print(user_tweets.output_file)

    #for t in user_tweets._tweets:
    #    print({'id_str':t.id_str})

    """
    for handle in ('pybites', 'techmoneykids', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
    """