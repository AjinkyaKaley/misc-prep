# Python3 program to find Maximum difference
# between two elements such that larger
# element appears after the smaller number

# The function assumes that there are
# at least two elements in array. The
# function returns a negative value if the
# array is sorted in decreasing order and
# returns 0 if elements are equal


def maxDiff(arr, n):

	# Initialize Result
	maxDiff = -1

	# Initialize max element from
	# right side
	maxRight = arr[n - 1]

	for i in range(n - 2, -1, -1):
		if (arr[i] > maxRight):
			maxRight = arr[i]
		else:
			diff = maxRight - arr[i]
			if (diff > maxDiff):
				maxDiff = diff
	return maxDiff


# Driver Code
if __name__ == '__main__':
	arr = [7, 1, 5, 3, 6, 4]
	n = len(arr)

	# Function calling
	print("Maximum difference is",
            maxDiff(arr, n))

# This code is contributed by 29AjayKumar
