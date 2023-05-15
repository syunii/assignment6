from math_function import *


def main():

    data_1 = int(input("Masukkan Input 1 : "))
    data_2 = int(input("Masukkan Input 2 : "))
    operator = input("Masukkan Operator (+ , * , /) : ")

    if operator == "+":
        result = add(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))

    elif operator == "*":
        result = multiplication(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))

    elif operator == "/":
        result = division(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))

    else:
        print("Maaf ya, operator belum terdaftar")


if __name__ == "__main__":
    print("Hello Main !")
    main()