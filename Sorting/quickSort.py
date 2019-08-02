class QuickSort:

    def partition(self, numbers, low, high):
        i = low-1
        pivot = numbers[high]
        for j in range(low, high):
            if numbers[j] <= pivot:
                i+=1
                numbers[i], numbers[j] = numbers[j], numbers[i]
        numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]
        return i+1 

    def quickSort(self, numbers, low, high):
        if low < high:
            partition_idx = self.partition(numbers, low, high)
            self.quickSort(numbers, low, partition_idx - 1)
            self.quickSort(numbers, partition_idx+1, high)

q = QuickSort()
_data = [10,16,8,12,15,6,3,9,5]
q.quickSort(_data, 0, len(_data) - 1)
print(_data)
