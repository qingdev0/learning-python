def even_odd():
    """document
    code reuse
    """
    n = input("[read] type a number: ")
    n = int(n)

    if n % 2 == 0:
        print("[info] the number is even.")
    else:
        print("[info] the number is odd.")


if __name__ == "__main__":
    even_odd()
    even_odd()
    even_odd()

#######
# EOF #
#######
