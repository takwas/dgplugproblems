#!/usr/bin/env python
#
# PROBLEM:
# --------
# 
# Take the 4 logs from the top of https://dgplug.org/irclogs/2016/
# and then try to find for each nick ever present in those files,
# who spoke with whom highest number of times.
#
# Like:
#     kushal spoke to avik 35 times
#     avik spoke to gkadam 55 times
#
# and like that, for all the nicks.

# standard library imports
import os


log_files = [os.path.join('logs', x) for x in os.listdir('logs')]
lines = list()


def readlines(file_):
    """Return a list of lines read from `file_`
    
    Clean the lines a bit before returning them.
    Note:
        It actually returns a generator of these lines.
    """
    with open(file_, 'r') as f:
        log_lines = (line.lower().strip() for line in f.readlines())
        return log_lines


# read all lines from log_files
for file_ in log_files:
    lines.extend(readlines(file_))


# get all nicks
lines = [line.split() for line in lines]
nicks = set([line[1].strip('<>') for line in lines])

conv = dict()


if __name__ == '__main__':
    for line in lines:
        nick = line[1].strip('<>')
        for token in line:
            if token in nicks:
                conv[nick, token] = conv.get((nick, token), -1) + 1

    for key in sorted(conv, key=lambda x: conv.get(x)):
        print conv.get(key), '\t', key