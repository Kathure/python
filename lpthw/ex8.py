#!/usr/bin/python
formatter = "%r %r %r %r" #variable with 4 placeholders
print formatter %(1,2,3,4) #prints 4 integers into the placehlder variable declared above
print formatter %("one" , "two","three","four") #prints four short strings into the placeholder variable
print formatter %(formatter, formatter,formatter,formatter) #prints the placeholders within themselves
print formatter %( #prints four longer strings into the placeholder variable
    "I had this thing.", #don't forget the commas
    "That you could type up right." ,
    "But it didn't sing." ,
    "So I said gooodnight"
)
