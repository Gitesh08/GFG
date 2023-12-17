class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		if n==1:
		    return arr[0]
		a, b = arr[0], arr[1]
		for i in range(2,n):
		    a, b = max(a,b), max(b, arr[i]+a)
		return max(a,b)
