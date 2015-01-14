#!/usr/bin/python
#coding:utf-8

filename = 'testfile.txt'
fp = open(filename,'w+')
content = """this is the test file.
hello world!
I love Python"""
fp.writelines(content)
fp.close()



fp = open('testfile.txt','r')



for eachline  in fp:
    print eachline


