class FibonacciRecursive:
    def calculate(self, n):
        if n <= 1:
            return n
        return self.calculate(n - 1) + self.calculate(n - 2)