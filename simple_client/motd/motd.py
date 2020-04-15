#!/usr/bin/env python3

import random
import time

DATAFILE = 'data.txt'
INDEXTEMPLATE = "index.template"
INDEXFILE = "index.html"
MOTD_MESSAGE = "MOTD_MESSAGE"
MOTD_AUTHOR = "MOTD_AUTHOR"

class MotdBook():
    def __init__(self, filename):
        self.debug = False
        self.book = []
        self.lines = 0
        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if  len(line.strip()) > 0:
                    self.lines += 1
                    self.book.append(line)
                if self.debug:
                    print("count:%d line:%s" % (self.lines, line))
            f.close()

    def getmotd(self):
        # Is this the best place to start randomize?
        random.seed(time.time())
        index = random.randint(0, self.lines - 1)
        if self.debug:
            print("lines:%d index:%d" % (self.lines, index))
        message, author = self.book[index].split('|')
        message.strip()
        author.strip()
        return message, author

    def getdate(self):
        datestr = time.strftime('%Y-%m-%d %a', time.localtime(time.time()))
        return datestr

def make_page(filename):
    motdbook = MotdBook(filename)
    message, author = motdbook.getmotd()

    try:
        fin = open(INDEXTEMPLATE, 'r')
        # nested 'try' does not seem to work
        #try:
        with open(INDEXFILE, 'w') as fout:
            while True:
                line = fin.readline()
                if not line:
                    break
                newline = line.replace(MOTD_MESSAGE, message)
                newline2 = newline.replace(MOTD_AUTHOR, author)
                fout.write(newline2)
    except Exception:
        print('Can not open input file: ' + INDEXTEMPLATE)

if __name__ == '__main__':
    """
    motdbook = MotdBook(DATAFILE)
    message, author = motdbook.getmotd()
    #print('MOTD (', end='')
    print(motdbook.getdate()) #+')')
    print()
    print(message)
    print('-', author) # , This is weird.. '-')
    #del motdbook
    """
    make_page(DATAFILE)
