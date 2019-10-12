class Heap():
    def insert_heap(self, arr, inx):
        while ((inx - 1) // 2) >= 0 and arr[inx] > arr[(inx - 1) // 2]:
            arr[inx], arr[(inx - 1) // 2] = arr[(inx - 1) // 2], arr[inx]
            inx = (inx - 1) // 2

    def heap_modify(self, arr, father, last):
        while 2 * father + 1 < last:
            child = 2 * father + 1
            if child + 1 < last and arr[child + 1] > arr[child]:
                child += 1
            if arr[child] <= arr[father]:
                break
            else:
                arr[father], arr[child] = arr[child], arr[father]
                father = child

    def heap_sort(self, arr):
        # 这里不能省，因为后面直接从顶开始向下沉当前元素。所以得首先保证整个树是大根堆。
        for i in range(1, len(arr)):
            self.insert_heap(arr, i)
        for i in range(len(arr) - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heap_modify(arr, 0, i)

if __name__ == '__main__':
    # arr = []
    # arr = [1]
    # arr = [1, 2]
    arr = [2, 3, 4, 1, 7, 6, 5]
    Heap().heap_sort(arr)
    print(arr)
