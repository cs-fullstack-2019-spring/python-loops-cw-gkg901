
def main():

    # ex1()
    # ex2()
    # ex3()
    ex4()

def ex1():
    for nums in range(-20,51,1):
        print(nums)



def ex2():
    for evens in range(0,21,2):
        print(evens)


def ex3():
    num1 = int(input("enter a number"))
    num2 = int(input("enter another number"))
    num3 = int(input("enter another number"))

    avg = (num1+num2+num3)/3

    print("The average of ",num1,"+", num2,"+",num3,"is ",str(avg))

def ex4():
    while True:
        pass1 = input("enter password. enter 'q' to quit")
        pass2 = input("confirm password. enter 'q' to quit")
        if pass1 == 'q':
            break
        elif pass2 == "q":
            break
    if pass1 == pass2:
        break





if __name__ == '__main__':
    main()
