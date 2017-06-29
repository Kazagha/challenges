import json
import sys
from textblob import TextBlob

def read_json(input_file):
    with open(input_file) as f:
        for line in f.readlines():
            yield json.loads(line)

def _get_tags(tweet_text):
    blob = TextBlob(tweet_text)
    return blob.tags

def _get_noun_phrases(tweet_text):
    blob = TextBlob(tweet_text)
    return blob.noun_phrases

def _get_sentiment(tweet_text):
    blob = TextBlob(tweet_text)
    return blob.sentiment

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('please provide json data file')
        sys.exit(1)
    input_file = sys.argv[1]
    tweets = read_json(input_file)

    # Pos, Neg, Count
    analysis = [0, 0, 0]

    for tw in tweets:
        #print(dict(tw)['text'])
        #print(get_tags(dict(tw)['text']))
        #print(_get_noun_phrases(dict(tw)['text']))
        print(f'{_get_sentiment(dict(tw)["text"]).polarity} / '
              f'{_get_sentiment(dict(tw)["text"]).subjectivity}  -   {dict(tw)["text"]}')

        if(_get_sentiment(dict(tw)["text"]).polarity > 0):
            analysis[0] += 1
        elif (_get_sentiment(dict(tw)["text"]).polarity == 0):
            pass
        else:
            analysis[1] += 1

        analysis[2] += 1

    print(f'Positive {(analysis[0]/analysis[2])*100}%')
    print(f'Negative {(analysis[1]/analysis[2])*100}%')