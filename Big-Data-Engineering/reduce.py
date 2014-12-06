#!/usr/bin/env python

import sys

current_word = None
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, _ = line.split('\t', 1)

    if current_word == word:
        continue
    else:
        print '%s\t%s' % (word, None)
        current_word = word
