def main():
    x = int(input("What's the value of X? "))
    print("x squared is --> ", square(x))

def square(n):
    return n*n

if __name__ == "__main__":  # "It will only run 'main()' if this file is executed directly"
    main()