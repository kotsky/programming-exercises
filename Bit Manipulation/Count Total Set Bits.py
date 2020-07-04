'''
Problem Description

Given a positive integer A, the task is to count the total number of set bits in the binary representation of all the numbers from 1 to A.

Return the count modulo 109 + 7.

Problem Constraints
1 <= A <= 109

Input Format
First and only argument is an integer A.

Output Format
Return an integer denoting the ( Total number of set bits in the binary representation of all the numbers from 1 to A )modulo 109 + 7.

Example Input
Input 1:

 A = 3
Input 2:

 A = 1

Example Output
Output 1:

 4
Output 2:

 1


Example Explanation
Explanation 1:

 DECIMAL    BINARY  SET BIT COUNT
    1          01        1
    2          10        1
    3          11        2
 1 + 1 + 2 = 4 
 Answer = 4 % 1000000007 = 4
Explanation 2:

 A = 1
  DECIMAL    BINARY  SET BIT COUNT
    1          01        1
 Answer = 1 % 1000000007 = 1
 '''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        A += 1
        
        power2 = 2
        count = A // 2;
        
        while power2 <= A:
            
            t = A // power2;
            
            # totalPairs/2 gives the complete  
            # count of the pairs of 1s.  
            # Multiplying it with the current power  
            # of 2 will give the count of  
            # 1s in the current bit  
            
            count += (t//2) * power2
            
            if ((A//power2) & 1):
                count += A % power2
            
            power2 <<= 1
        
        return count

  
