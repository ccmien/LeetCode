class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        """
        You are climbing a stair case. It takes n steps to reach to the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for _i in xrange(n-3):
            a, b = b, a+b
        return a+b