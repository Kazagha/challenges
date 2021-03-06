from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""

    with open(RSS_FEED) as rrs:
        rrs_text = (' '.join(line.lower().replace('-', ' ') for line in rrs))

    return TAG_HTML.findall(rrs_text)

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""

    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""

    return ((x,y) for x in tags for y in tags if x != y if similar_tags((x,y)))

def similar_tags(tags):
    """Return True if the pair of tags are similar 
         
         
    """

    return (SequenceMatcher(a=tags[0], b=tags[1]).ratio()) > SIMILAR

if __name__ == "__main__":

    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('Top tags')
    print(', '.join(tag[0] for tag in top_tags))

    #print(similar_tags(('challenge', 'challenges')))
    #print(list(t for t in get_similarities(set(tags))))
    print("Similar Tags")
    for t in get_similarities(set(tags)):
        print(f'{repr(t[0]).ljust(25 )}{repr(t[1]).ljust(10)}')

    """
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
    """