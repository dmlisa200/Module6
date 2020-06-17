def multiply_string(my_name, num):
    """prints the string name the num times
    :param my_name, input name
    :param num, favorite number between 1 and 9
    returns: the input name printed as many times as the number entered
    raises ValueError:  raises an Error
    """
    my_name = input("What is your name? ")
    num = int(input("What is your favorite number between 1 and 9? "))
    return my_name * num


if __name__ == '__main__':
    try:
        message = multiply_string('lisa', 1)
    except ValueError as err:
        print("ValueError has occurred")
    else:
        print(message)
