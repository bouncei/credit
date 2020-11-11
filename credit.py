# import get_int and get_string libaries from cs50
import sys

def main():
    first_sum = 0  # iniitialize the first sum
    second_sum = 0 # initialize the second sum
    
    

    # prompt the user for an input
    n = input("Credit Card Number: ")

    # defininig the length of the credit card number to counter
    counter = len(str(n))

    # a condition that dictates if the input is a credit card number
    if counter != 13 and counter != 15 and  counter != 16:
        print("INVALID")     # returns an error if its not a credit card number
        sys.exit()


    # Calculate first sum
    for i in range(-2, (-counter-1), -2):
        # initializing a temporary module
        tmp_module = int(n[i]) * 2

        if tmp_module >= 10:
            first_sum = first_sum + tmp_module - 9

        else:
            first_sum = first_sum + tmp_module

    for i in range(-1, (-counter-1), -2):
        # initializing a temporary odd module
        tmp_odd = int(n[i])
        second_sum = second_sum = tmp_odd


    # summing the first sum and second sum to et the total
    total = first_sum + second_sum

    # Check Luhn Algorithm
    if total % 2 == 0:
        # check the first two digits if its an Amex card
        if int(n[0]) == 3 and int(n[1]) == 4 or int(n[1]) == 7:
            print("AMEX")   # return successful if its an Amex card

        # check the first two digits if its a Mastercard
        elif int(n[0]) == 5 and int(n[1]) == 1 or int(n[1]) == 2 or int(n[1]) == 3 or int(n[1]) == 4 or int(n[1]) == 5:
            print("MASTERCARD")  # return successful if its an Amex card

        # check the first digit if its a Visa card
        elif int(n[0]) == 4:
            print("VISA")  # return successful if its an Amex card

        else:
            print("INVALID")  # return an error if the alogorithm doesn't match as a credit card



if __name__ == "__main__":
    main()