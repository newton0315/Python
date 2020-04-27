#!/usr/bin/env python3

import random
import time
import http.server
import socketserver

import threading

handler = http.server.SimpleHTTPRequestHandler

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
        with open(filename, 'r', encoding='utf-8') as f:
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

class QuizBook(MotdBook):
    def __init__(self, filename):
        self.debug = False
        self.book = []
        self.lines = 0
        with open(filename, 'r', encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if  len(line.strip()) > 0 and line == '==':
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

def make_motd_page(book):
    while True:
        message, author = book.getmotd()
#        print("new message:" + message, "new author:" + author)

        try:
            fin = open(INDEXTEMPLATE, 'r')
            # nested 'try' does not seem to work
            #try:
            fout = open(INDEXFILE, 'w', encoding='utf-8')
            while True:
                line = fin.readline()
                if not line:
                    break
                newline = line.replace(MOTD_MESSAGE, message)
                newline2 = newline.replace(MOTD_AUTHOR, author)
                fout.write(newline2)
            fout.close()
            fin.close()
        except Exception:
            print('Can not open input file: ' + INDEXTEMPLATE)
        time.sleep(60)
'''
if __name__ == '__main__':
    motdbook = MotdBook(DATAFILE)
    while True:
        ts = threading.Thread(target=make_page, args=(motdbook,))
        ts.start()
        time.sleep(5)
    #print('MOTD (', end='')
    #print(motdbook.getdate()) #+')')
    #print()
    #print(message)
    #print('-', author) # , This is weird.. '-')
'''

with socketserver.TCPServer(('', 10001), handler) as httpd:
    motdbook = MotdBook(DATAFILE)
    ts = threading.Thread(target=make_motd_page, args=(motdbook,))
    ts.start()
    print('Server listening on port 10001...')
    httpd.serve_forever()
