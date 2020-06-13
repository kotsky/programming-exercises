'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''
class K:
    def __init__(self, obj, *args):
        self.obj = obj
    def __lt__(self, other):
        return '%d%d'%(self.obj,other.obj) < '%d%d'%(other.obj,self.obj)


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(A)
        B=[]
        C=[]
        s1=""
        l=len(str((max(A))))
        for i in A:
            s=""
            l1=len(str(i))
            if(l1<l):
                s=s+str(i)+(l-l1)*str(i)[l1-1]
            else:
                s=s+str(i)
            B.append(int(s))
        C = B.copy()
        while(len(B)>0):
            m=max(B)
            n=C.index(m)

            s1=s1+str(A[n])
            B.remove(m)
            C[n] = -1
        if(int(s1)==0):
            return 0
        else:
            return s1
