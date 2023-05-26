# x= input("enter the value")
# y= input ("enter the value")

# print ("x + y")
# print (int(x) + int(y))

# or
# x= int(input("enter the value"))
# y= int(input ("enter the value"))
# print (x + y)
# print(f"{z:02d}")
# e.g. for displaying the resut 2 as 02

# x= float(input("enter the value"))
# y= float(input ("enter the value"))

# z= round(x + y, 2)
# print (z)

# or
# z= x + y
# print (f"{z:.2f}")


#for numeric formatting(automatically prints comma after 3 numbers from left side)
# print (f"{z:,}")

def main():
    x=int(input("What's x? "))
    print("x sqrared is", square(x))

def square(n):
        return n**2
# or
    # return pow(n, 2)
main()

