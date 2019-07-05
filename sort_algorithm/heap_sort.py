class Heap():
    def insert_heap(self, arr, inx):
        while ((inx - 1) // 2) >= 0 and arr[inx] > arr[(inx - 1) // 2]:
            arr[inx], arr[(inx - 1) // 2] = arr[(inx - 1) // 2], arr[inx]
            inx = (inx - 1) // 2

    def heap_modify(self, arr, inx, size):
        while 2 * inx + 1 < size:
            child = 2 * inx + 1
            if child + 1 < size and arr[child + 1] > arr[child]:
                child += 1
            if arr[child] <= arr[inx]:
                break
            else:
                arr[inx], arr[child] = arr[child], arr[inx]
                inx = child

    def heap_sort(self, arr):
        # build heap
        for i in range(1, len(arr)):
            self.insert_heap(arr, i)
            print(arr[:i + 1])

        # swap heap top and last heap left, then, modify the heap
        for i in range(len(arr) - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heap_modify(arr, 0, i)


if __name__ == '__main__':
    arr = [2, 3, 4, 1, 7, 6, 5]
    Heap().heap_sort(arr)
    print('res:')
    print(arr)
