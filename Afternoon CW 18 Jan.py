
def main():

    # ex1()
    # ex2()
    # ex3()
    # ex4()
    bonus()

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
        pass1 = input("enter password")
        pass2 = input("confirm password. enter 'q' to quit.")
        if pass1 == pass2:
            break

        elif pass2 == "q" or pass1 == "q":
            break


def bonus():
    endValue = int(input("enter a number"))
    for i in range(1,endValue+1):
        print(i)
        if i % 3 == 0 and i % 5 == 0:
            print("FIZZBUZZ " + str(i))

        elif i % 3 == 0:
            print("FIZZ " + str(i))

        elif i % 5 == 0:
            print("BUZZ " + str(i))



        else:
            print(endValue)



if __name__ == '__main__':
    main()
