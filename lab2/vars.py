#!/usr/bin/env python3

# a file that takes two cmd lines and prints the variables


import sys

name = sys.argv[0]
args = sys.argv[1:]

def printhippo(name, args):
    print("Script name: ", name)
    print("name and variables: ", name, *args)


printhippo(name,args)
