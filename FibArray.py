class FibonacciArray:
    def calculate(self, n):
        fibs = [0] * (n + 1)
        fibs[0], fibs[1] = 0, 1
        for i in range(2, n + 1):
            fibs[i] = fibs[i - 1] + fibs[i - 2]
        return fibs