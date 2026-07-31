class Fibonacci:

    def __init__(self, n):
        self.n = n

    # Recursive Method
    def recursive(self, n):
        if n <= 1:
            return n
        return self.recursive(n - 1) + self.recursive(n - 2)

    # Dynamic (Iterative) Method
    def dynamic(self):
        if self.n <= 1:
            return self.n

        a, b = 0, 1
        for _ in range(2, self.n + 1):
            a, b = b, a + b
        return b

    # Display Fibonacci Series
    def display_sequence(self):
        series = []
        a, b = 0, 1

        for _ in range(self.n):
            series.append(a)
            a, b = b, a + b

        return series


def main():
    n = int(input("Enter the value of n: "))

    fib = Fibonacci(n)

    print("\nFibonacci Series:")
    print(fib.display_sequence())

    print("\nRecursive Result:")
    print(fib.recursive(n))

    print("\nDynamic Result:")
    print(fib.dynamic())


if __name__ == "__main__":
    main()