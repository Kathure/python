#!/usr/bin/python
elizabeth = {
    "name" : "moringa",
    "age": 20,
    "height": 57,
    "weight": "181lbs"

}
def printbefore(x):
    for key in x:
        print key, x[key]

def replace(x):
    for key in x:
        if key == "name":
            x[key]= "school"
        print key , x[key]
printbefore(elizabeth)
replace(elizabeth)
