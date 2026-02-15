num1 = 100

def my_add_function(n, m):
    """
        This is a function that adds two input numbers.
    """
    return n + m

def main():
    print(f"Value of num1: {num1}")

    result = my_add_function(50, 75)
    print(f"Result of 50 + 75 = {result}")

    print(__name__)

if __name__ == "__main__":
    main()