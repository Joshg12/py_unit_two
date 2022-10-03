# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


name = input("What's your name?")

print ("That is a nice name",name)

place = input("Where are you from?")

if "maryland" in place:
    print("Me too!")

else:
    print("That is cool, I am from Maryland.")


number = input("What is your favorite number?")

if "33" in number:
    print("Me too!")

difference = 33 - int(number)

print ("The difference is" , difference)



house = input("What is your dream house?")

if "some type of mansion" in house:
    print("Me too!")

else:
    print("That is a nice choice.")

cost = input("How much does your dream house cost?")


if int(cost) > 50000:
    print("That is expensive.")

else:
    print("That is a good deal.")

loanlegnth = int(input("How long will the loan last in years?" ))


intrestrate = float(input("What is the interest rate on this purchase?"))

p = float(cost)
r = intrestrate

n = loanlegnth * 12

mpymnt = (r * p) / (1 - (1+r) ** -n)


#print ("Your monthly payment for" + house + "is" + mpymnt + "That is a total of" + (mpymnt * n) + "Goodbye" + name)


print ("Your monthly payment for" , house , "is" , mpymnt , "That is a total of" , (mpymnt * n) , "Goodbye" , name)

