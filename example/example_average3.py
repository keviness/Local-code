# average3.py


def main():

    sum = 0.0
    count = 0
    x = eval(input("Enter a number(negative to quit) :"))
    while x >= 0:
        sum += x
        count += 1
        

    print("\n The average of the numbers is:", sum/count)
 
main()