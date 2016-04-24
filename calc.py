num1 = raw_input("first number")
num2 = raw_input("second number")
operation = raw_input("what would you like to do ")
if str(operation) == "add" :
    print int(num1) + int(num2)
elif str(operation) == "multiply" :
    print int(num1) * int(num2)
elif str(operation) == "divide" :
    print int(num1)//int(num2)
else :
    print "thank you for your time"
