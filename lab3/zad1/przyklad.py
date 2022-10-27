def foo(i: int) -> None:
    if i < 0:
        return

    print(i)

    foo(i - 1)


foo(10)
