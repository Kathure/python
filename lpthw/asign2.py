#!/usr/bin/python
vegetables= ["lettuce","tomato","carrots","onions"]

def replace(y):
    print y
    for i in y:
        if i == "tomato":
            print "a tomato isn't a vegetable"
            y.pop(1)
            y.append("kales")
            print y
            print "there much better"

replace(vegetables)
