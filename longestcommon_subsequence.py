def recursive(a,b,n,m):
	if n==0 or m==0:
		return 0
	if a[n-1]==b[m-1]:
		return (1 + recursive(a,b,n-1,m-1))
	else:
		return max(recursive(a,b,n,m-1),recursive(a,b,n-1,m))
def recursive1(dp,a,b,n,m):
	if n<=0 or m<=0:
		return 0
	if dp[n][m]!=-1:
		return dp[n][m]
	if a[n]==b[m]:
		return 1+dp[n-1][m-1]
	else:
		dp[n][m]= max(dp[n][m-1],dp[n-1][m])
		return dp[n][m]
def recursive2(dp,a,b,n,m):
	
	for i in range(n+1):
		for j in range(m+1):
			if i==0 or j==0:
				dp[i][j]=0
			elif a[i-1]==b[j-1]:
				dp[i][j]=1+dp[i-1][j-1]
			else:
				dp[i][j]=max(dp[i-1][j],dp[i][j-1])
	return dp[n][m]
# Dynamic Programming implementation of LCS problem 

def lcs(X, Y,m,n): 
 
	L = [[None]*(n + 1) for i in range(m + 1)] 

	
	for i in range(m + 1): 
		for j in range(n + 1):
			if i == 0 or j == 0 : 
				L[i][j] = 0
			elif X[i-1] == Y[j-1]: 
				L[i][j] = L[i-1][j-1]+1
			else: 
				L[i][j] = max(L[i-1][j], L[i][j-1]) 

	# L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
	return L[m][n] 

	
a=input()
b=input()
dp=[[-1]*(len(a)+1)]*(len(b)+1)
print(dp)
print(recursive1(dp,a,b,len(a)-1,len(b)-1))
print(lcs(a,b,len(a),len(b)))
print(recursive(a,b,len(a),len(b)))

print(recursive2(dp,a,b,len(a),len(b)))
