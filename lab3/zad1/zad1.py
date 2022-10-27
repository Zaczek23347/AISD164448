def foo(i: int) -> None:
    if i < 0:
        return

    print(i)

    foo(i - 1)

n = int(input("podaj n"))
foo(n)