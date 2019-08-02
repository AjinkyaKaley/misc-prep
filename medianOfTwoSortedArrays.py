# A Simple Merge based O(n) Python 3 solution
# to find median of two sorted lists

# This function returns median of ar1[] and ar2[].
# Assumptions in this function:
# Both ar1[] and ar2[] are sorted arrays
# Both have n elements


def getMedian(ar1, ar2, n):
    i = 0
    j = 0
    m1 = -1
    m2 = -1
    count =  0
    while count < n + 1:
        count += 1
        
        if i == n:
            m1 = m2
            m2 = ar1[0]
            break
        
        if j == n:
            m1 = m2
            m2 = ar2[0]
            break

        if ar1[i] < ar2[j]:
            m1 = m2
            m2 = ar1[i]
            i += 1
        elif ar1[i] > ar2[j]:
            m1 = m2
            m2 = ar2[j]
            j += 1
    return (m1+m2)/2
        
def findMedian(arr):
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2] + arr[(n - 1)//2]) // 2
    return arr[n // 2]
    
def getMedianOptimal(arr1, arr2, n):
    if n == 2:
        return (max(arr1[0], arr2[0])+min(arr1[1], arr2[1]))//2
    m1 = findMedian(arr1)
    m2 = findMedian(arr2)

    if m1 > m2:
        if n % 2 == 0:
            return getMedianOptimal(arr1[:int(n / 2) + 1], arr2[int(n / 2) - 1:], int(n / 2) + 1)
        else:
            return getMedianOptimal(arr1[:int(n / 2) + 1],
                             arr2[int(n / 2):], int(n / 2) + 1)
    else:
        if n % 2 == 0:
            return getMedianOptimal(arr1[int(n / 2 - 1):], arr2[:int(n / 2 + 1)], int(n / 2) + 1)
        else: 
            return getMedianOptimal(arr1[int(n / 2):], arr2[0:int(n / 2) + 1], int(n / 2) + 1) 
  

# Driver code to test above function
ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]
n1 = len(ar1)
n2 = len(ar2)
if n1 == n2:
	print("Median is ", getMedianOptimal(ar1, ar2, len(ar1)))
else:
	print("Doesn't work for arrays of unequal size")

# This code is contributed by "Sharad_Bhardwaj".
