import math

class FibonacciBinet:
    def calculate(self, n):
        phi = (1 + math.sqrt(5)) / 2
        psi = (1 - math.sqrt(5)) / 2
        return round((phi ** n - psi ** n) / math.sqrt(5))