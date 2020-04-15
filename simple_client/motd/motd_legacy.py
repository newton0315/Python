# -*- coding: utf-8 -*-

import random
import time

DATAFILE = "data.txt"

book = []
  
def print_book(pages):
    for i in pages:
       print(i[0] + " by " + i[1])

def make_book(filename, messages):
    count = 0
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if line:
                messages.append(line)
                count += 1
            else:
                break
        f.close()
        return count

def make_book2(str):
    mset = []
    msg, author=map(str.strip, s.split(','))
    mset.append(msg)
    mset.append(author)
    book.append(mset)

def select_msg(book, maxnum):
    random.seed(time.time())
    choice = random.randint(0, maxnum)
    return book[choice]

def do_motd(message):
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    print(str(message))

def run():
    book = []
    numlines = make_book(DATAFILE, book)
    motd = select_msg(book, numlines)
    do_motd(motd)

if __name__ == '__main__':
    run()

