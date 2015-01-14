#!/usr/bin/python
#coding=utf8

class AddrBookEntry(object):
    "address book entry class"
    
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        print "Created instance for %s" % self.name

    def UpdatePhone(self,newph):
        self.phone = newph
        print "updated phone for %s" % self.name


zhang = AddrBookEntry('zhang','82828587')
print zhang.phone
print zhang.phone