# -*- coding: utf-8 -*-

# Equivalents file class
#
# Pedro Morais <morais@kde.org>
# José Nuno Pires <jncp@netcabo.pt>
# (c) Copyright 2003, 2004
# Distributable under the terms of the GPL - see COPYING

class Equivalent:

    def __init__(self):
        self.map = None

    def read_lines(self, filename):
        try:
            file = open(filename)
            lines = file.readlines()
            file.close()
            return lines
        except IOError:
            return None
        
    def parse(self, filename, strip = ''):
        lines = self.read_lines(filename)
        if lines == None: return 0
        if self.map == None: self.map = {}
        msgid = None
        list = []
        for i in lines:
            i = i.strip()
            for k in strip: i = i.replace(k, '')
            if len(i) == 0:
                if msgid != None and len(list) > 0: self.map[msgid] = list
                msgid = None
                list = []
            elif msgid == None:
                msgid = i
            else:
                list.append(i)
        if msgid != None and len(list) > 0: self.map[msgid] = list
        return 1

    def check(self, msgid, result):
        if self.map == None or not self.map.has_key(msgid): return 0
        eq = self.map[msgid]
        for i in result:
            if not(i in eq): return 0
        return 1
