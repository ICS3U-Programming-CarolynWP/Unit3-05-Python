#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/10/13
# Asks the user to enter an integer from 1-12
# And displays the month associated with the integer


def find_month(month):
    month_number = {
        1: "{} Is January!".format(month),
        2: "{} Is February!".format(month),
        3: "{} Is March!".format(month),
        4: "{} Is April!".format(month),
        5: "{} Is May!".format(month),
        6: "{} Is June!".format(month),
        7: "{} Is July!".format(month),
        8: "{} Is August!".format(month),
        9: "{} Is September!".format(month),
        10: "{} Is October!".format(month),
        11: "{} Is November!".format(month),
        12: "{} Is December!".format(month),
    }
    return month_number.get(month, "That input is invalid")


if __name__ == "__main__":
    # title of the program
    print("Months")
    # user input for the month
    month_number = int(
        input("Enter an integer from 1-12 and " " get the corresponding month: ")
    )
    print(find_month(month_number))
