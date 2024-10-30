import math
print("Instructions on Paint Can : \n1 Can of paint can cover 5 square meters.\n")
def num_can(length, breadth,cover):
    return math.ceil((length*breadth)/cover)
l = int(input("Length of the wall : "))
b = int(input("Breadth of the wall : "))
unit = 5
print('No. of Cans required to pain the whole wall is : ',num_can(length = l, breadth=b, cover=unit))

