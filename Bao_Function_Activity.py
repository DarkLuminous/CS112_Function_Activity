from sys import exit

while True:
    num1 = int(input("Enterfirst number:"))
    num2 = int(input("Entersecond number:"))
    num3 = int(input("Enterthird number:"))


    def mult123(num1, num2, num3):
        ans = num1 * num2 * num3
        print(f"Result is {ans}\n")

    def mult12(num1, num2, num3):
        ans = num1 * num2 + num3
        print(f"Result is {ans}\n")

    def mult13(num1, num2, num3):
        ans = num1 * num3 + num2
        print(f"Result is {ans}\n")

    def mult23(num1, num2, num3):
        ans = num2 * num3 + num1
        print(f"Result is {ans}\n")

    def addAll(num1, num2, num3):
        ans = num2 + num3 + num1
        print(f"Result is {ans}\n")

    def main():
        if num1 == num2 == num3:
            mult123(num1, num2, num3)

        elif num1 == num2:
            mult12(num1, num2, num3)

        elif num1 == num3:
            mult13(num1, num2, num3)

        elif num2 == num3:
            mult23(num1, num2, num3)

        else:
            addAll(num1, num2, num3)

    main()

    while True:
        print("input [0] to EXIT!")
        cont = input()

        InpCheck = cont.isdigit()  # check input if number if valid

        if InpCheck == False:
            break
            main()

        elif int(cont) == 0:
            print("Thank You!")
            exit()

        else:
            break
            main()