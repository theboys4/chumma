def lis(a,n):
	arr=[1]*n
	for i in range(1,n):
		for j in range(i):
			if a[i]>a[j] and arr[j]+1>arr[i]:
				arr[i]=arr[j]+1
	return max(arr)
a=[4,56,3,35,36,54,5,47,4]
print(lis(a,len(a)))