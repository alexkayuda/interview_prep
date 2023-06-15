
def print_Fib_seq(number: int) -> None:
    a,b = 0,1
    while a < number:
        print(a, end=" ")
        a,b = b, b+a
    print()


def get_Fib_seq(number: int) -> list[int]:
    seq = []

    a,b, = 0,1
    while a < number:
        seq.append(a)
        a,b = b, b+a

    return seq


if __name__ == "__main__":
    print_Fib_seq(100)

    print(get_Fib_seq(100))