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
            #yield match.group(0).strip('import').strip(' ')
            yield match.group(1)

def gen_count(lines):
    lines = sorted(lines)

    _line = None
    line_count = 0

    for line in lines:

        if(line == _line):
            # line is the same as the _line, increment and do not return a value
            line_count = line_count + 1
        else:
            # New line value, return the count and _line
            yield f'{line_count} {_line}'

            # Reset the count and _line variable
            _line = line
            line_count = 1

def gen_sort(lines):
    for line in (sorted(lines, reverse=True)):
        yield line

if __name__ == "__main__":
    #regex_exp = r'(import|from) \b.*\b( import)*'
    #regex_exp = r'import \b.*\b'
    regex_exp = r'import (\w+)'
    PATTERN = re.compile(regex_exp)
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    lines = gen_grep(lines, PATTERN)
    lines = gen_count(lines)
    lines = gen_sort(lines)

    for line in lines:
        print(line)
