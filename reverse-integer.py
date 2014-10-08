class Solution:
    # @return an integer
    def reverse(self, x):
    	"""
    	Reverse digits of an integer.

		Example1: x = 123, return 321
		Example2: x = -123, return -321

		"""
        if x == 0:
            return 0
        else:
            return x/abs(x) * int(str(abs(x))[::-1])