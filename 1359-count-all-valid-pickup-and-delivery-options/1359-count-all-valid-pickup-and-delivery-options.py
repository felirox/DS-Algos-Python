from math import factorial
class Solution:
    def countOrders(self, n: int) -> int:
        Pperm=factorial(n)
        Dcombo=1
        for i in range(1,n+1):
            Dcombo*=(2*i-1)
        return (Pperm*Dcombo)%(10**9+7)