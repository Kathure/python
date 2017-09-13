#!/usr/bin/python
from sys import argv #imports the argv module

script, filename = argv #unpacks argv so that it gets assigned to variables script and filename

txt = open(filename) #opens the text file

print "Here's your file %r:" %filename #prints the name of the file
print txt.read() #prints the content of the text file


print "Type the filename again:" #prints string
file_again = raw_input(">") #takes filename

txt_again = open(file_again) #opens file named above

print txt_again.read() #prints content of file named above
