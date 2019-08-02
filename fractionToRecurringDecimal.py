class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        self.remainderSet = set()
        self.quotientTillNow = ""

        def calculate(numerator, denominator):

            remainder = numerator % denominator
            quotient = numerator/denominator

            if quotient.is_integer():
                return ""+quotient
            if remainder in self.remainderSet:
                return self.quotientTillNow+quotient
            return calculate(remainder, denominator)

        calculate(numerator,denominator)