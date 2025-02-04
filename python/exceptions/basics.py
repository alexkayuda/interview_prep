def divide(x: int, y: int):
    try:
        result = x / y 
    except ZeroDivisionError as err:
        print(f"Inside ZeroDivisionError Exception and the error is: {err}")
    except FileNotFoundError as err:
        print(f"Inside FileNotFoundError Exception and the error is: {err}")
    # except:
    #     print(f"Inside General Exception. Don't know what happened...")
    else:
        print(f"Sooo... Calculations went well and the result is {result}")
    finally:
        print("No Matter what, I will always be here")


if __name__ == "__main__":
    print(divide(8, 2))
    print("\n")
    print(divide(8, 0))