import glob
import re

"""
Turn the following unix pipeline into Python code using generators

$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""

def gen_files(pat):
    for file_name in glob.glob(pat):
        yield file_name

def gen_lines(files):
    for file_name in files:
        with open(file_name) as text:
            for line in text:
                yield line


def gen_grep(lines, pattern):
    for line in lines:
        for match in pattern.finditer(line):
            yield match.group(0)


def gen_count(lines):
    pass


if __name__ == "__main__":
    regex_exp = r'(import|from) \b.*\b( import)*'
    PATTERN = re.compile(regex_exp)
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    lines = gen_grep(lines, PATTERN)


    for line in lines:
        print(line)


