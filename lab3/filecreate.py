#!/usr/bin/env python3



def namefile():
    namehippo = input("What's your name: ")
    file = namehippo + ".txt"
    with open(file,"w") as pachyderm:
        pachyderm.write("This is the story of " + namehippo)

namefile()


def helloWorld():
    print("Hello World")

helloWorld()
