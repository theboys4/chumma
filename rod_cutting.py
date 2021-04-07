def mac(n,a,b,c):
	#print(n)
	if n<0:
		return -1
	if n==0:
		return 0
	a=max(mac(n-a,a,b,c),mac(n-b,a,b,c),mac(n-c,a,b,c))
	if a==-1:
		return a
	return a+1
def mac1(n,a,b,c):
	dp=[-1]*(n+1)
	dp[0]=0
	for i in range(1,n+1):
		if i-a>=0:
			dp[i]=max(dp[i],dp[i-a])
		if i-b>=0:
			dp[i]=max(dp[i],dp[i-b])
		if i-c>=0:
			dp[i]=max(dp[i],dp[i-c])
	return dp	
print(mac(23,11,9,12))
print(mac1(23,11,9,12))