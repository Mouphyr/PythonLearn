import random

class InitData:
    def __init__(self, n):
        """
        n是排序数的数量
        :param n:
        """
        self.len=n
        self.arr = [0]*n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

class Qsort(InitData):
    def partition(self,left,right):
        arr=self.arr
        k=i= left
        random_pos=random.randint(left,right) # 随机选一个数，避免陷入最坏时间复杂度
        arr[right],arr[random_pos]=arr[random_pos],arr[right]
        for i in range(left,right):
            if arr[i]<arr[right]:
                arr[k],arr[i]=arr[i],arr[k]
                k+=1
        arr[k],arr[right]=arr[right],arr[k]
        return k

    def qsort(self,left,right):
        if left<right:
            pivot=self.partition(left,right)
            self.qsort(left,pivot-1)
            self.qsort(pivot+1,right)

#堆排序
class HeapSort(InitData):
    def adjust_max_heap(self,pos,arr_len):
        """
        把某个子树调整为大根堆
        :param pos: 被调整的元素位置（父结点）
        :param arr_len: 列表长度
        :return:
        """
        arr=self.arr
        dad=pos
        son=dad*2+1 # 值更大的孩子（默认为左孩子）
        while son<arr_len:
            # 右孩子存在，且右孩子大于左孩子
            if son+1<arr_len and arr[son]<arr[son+1]:
                son+=1
            if arr[son]>arr[dad]:
                arr[dad],arr[son]=arr[son],arr[dad]
                # 继续调整son的子树
                dad=son
                son=dad*2+1
            else:
                break

    def heap_sort(self):
        """
        把列表调整为大根堆,此时堆顶元素即为最大元素
        :return:
        """
        # 将列表调整为大根堆
        for i in range(self.len//2-1,-1,-1):
            self.adjust_max_heap(i,self.len)
        arr=self.arr
        arr[0],arr[self.len-1]=arr[self.len-1],arr[0] #交换堆顶元素与最后元素
        # 处理完第一个元素后，每次只需调整交换后的堆顶元素即可
        for arr_len in range(self.len-1,1,-1):
            self.adjust_max_heap(0,arr_len)
            arr[0],arr[arr_len-1]=arr[arr_len-1],arr[0]

if __name__ == '__main__':
    sort_data=Qsort(10)
    sort_data.random_data()
    print("原始数据1为：",sort_data.arr)
    sort_data.qsort(0,sort_data.len-1)
    print("快排后数据为：",sort_data.arr)

    sort_data_2=HeapSort(10)
    sort_data_2.random_data()
    print("原始数据2 为：",sort_data_2.arr)
    sort_data_2.heap_sort()
    print("堆排序后数据为：",sort_data_2.arr)