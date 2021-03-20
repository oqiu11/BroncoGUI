# Olivia Qiu
# Ford Internship Question


# Checks to see if the parameter is an integer. If it is it will return true.
# Otherwise it will print an error statement and return false.
def int_check(x):

    try:
        # cast param to an int
        x = int(x)
        # if we wanted it to accept doubles like 3.0 or 3.2 we could just make it x = float(x)
        return True
    except ValueError:  # if casting fails
        print("Not An Integer!")
        return False


# Displays Statements depending on whether or not param is divisible by 3, 5, both, or neither.
def mustang_bronco(x):
    if x % 3 == 0 and x % 5 == 0:  # divisible by both 3 and 5
        print("MustangBronco")
    elif x % 3 == 0:  # divisible by 3
        print("Mustang")
    elif x % 5 == 0:  # divisible by 5
        print("Bronco")
    else:
        print(x)


def main():
    # accept an input
    x = input("Please Input an Integer: ")
    # Generally speaking the input command should run until an acceptable input has been given.
    # I was unsure what the instructions wanted.
    # If I wanted it to loop until it got an acceptable input I would do the following
    # while not int_check(x):
    #   x = input("Please Input an Integer: ")
    # then delete the following condition check. (Keep the contents!)
    if int_check(x):  # when x is an int cast x to an into and then call mustang bronco.
        x = int(x)
        mustang_bronco(x)


if __name__ == "__main__":
    main()

