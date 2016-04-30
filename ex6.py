x = "There are %d types of people." %10 #variable x takes in the string statement , %d is a plceholder for the double value 10
binary = "binary" # variable binary takes in the string "binary"
do_not = "don't" #variable do_not is assigned the string "don't"
y = "Those who know %s and those who %s" % (binary, do_not) #variable y is assigned the string statement , %s is a placeholder for sting vars binary and do_not

print x #prints vraiable x
print y #prints variable y

print "I said: %r. " %x   # prints string x inside another string %r is a placeholder for  string x
print "I also said: '%s'." %y  #prints string y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious


w = "This is the left side of ..."
e = "a string with a right side"

print w + e
