#!/usr/bin/python
name = raw_input("Who are you ?")
age = int(raw_input("How old are you"))
elizabeth = {
    "name" : "moringa",
    "age": 20,
    "height": 57,
    "weight": "181lbs"

}
def manipulater(x,y,z,*a):
    print x ,
    def doubler(y):
        return y *2

    for key in z:
        if key == "name":
            z[key]= "school"
        print key , z[key] ,
    print a

    manipulater(name, age,elizabeth, "female")
