#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: October 2019
# This program shows the factorial of a number


def main():
    while True:
        # input
        sub_answer = 1
        total_number = 1
        number = input("Input A Positive (+) Number: ")
        print()

        try:
            number_as_number = int(number)
            while number_as_number > sub_answer:
                # process
                print("x {0}".format(sub_answer))
                sub_answer = sub_answer + 1
                total_number = sub_answer * total_number

            print("x {0}".format(number_as_number))
            print("The answer is {0}".format(total_number))

        except ValueError:
            print()
            print("Invalid Input")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
