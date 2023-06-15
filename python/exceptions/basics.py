def divide(x: int, y: int):
    try:
        result = x / y
    except ZeroDivisionError as err:
        print(err)
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


if __name__ == "__main__":
    #divide(8, 2)
    divide(8, 0)