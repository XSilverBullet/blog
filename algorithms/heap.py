global a
a = [4, 5,9, 6,3]
def insert(a, current, low, high):
    large = 2 * low + 1

    while large <= high:
        if large < high and a[large] < a[large + 1]:
            large += 1
        if current > a[large]:
            break
        else:
            a[low] = a[large]
            low = large
            large = 2 * low + 1

    a[low] = current


def build_heap(a):
    for i in range(int(len(a) / 2 - 1), -1, -1):
        current = a[i]
        insert(a, current, i, len(a) - 1)


def heap_sort(a):
    build_heap(a)
    for last_unsorted in range(len(a) - 1, 0, -1):
        current = a[last_unsorted]
        a[last_unsorted] = a[0]
        insert(a, current, 0, last_unsorted - 1)


build_heap(a)
print(a)

heap_sort(a)
print(a)

#稳定排序：插入，冒泡，归并
#所谓稳定性是指待排序的序列中有两元素相等,排序之后它们的先后顺序不变