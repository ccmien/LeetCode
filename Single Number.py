class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        my_dict = {}
        for i in range(len(A)):
            if str(A[i]) not in my_dict:
                my_dict[str(A[i])] = 0
            my_dict[str(A[i])] += 1
        return [int(i) for i in my_dict if my_dict[i] == 1][0]