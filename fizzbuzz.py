num1 = raw_input("enter a number: ")
if float(num1)%3 == 0 and float(num1)%5 == 0:
    print "FizzBuzz"
elif float(num1)%3 == 0:
    print "Fizz"
elif float(num1)%5 == 0:
    print "Buzz"

else :
    print(float(num1))
