# 归并排序算法实现

def merge_sort(arr):
    if len(arr) <= 1:
        return arr   # 数组长度为1或0，直接返回
    mid = len(arr) // 2   # 数组长度的一半
    left = arr[:mid]   # 左半部分数组
    right = arr[mid:]   # 右半部分数组
    left = merge_sort(left)   # 递归调用左半部分数组进行排序
    right = merge_sort(right)   # 递归调用右半部分数组进行排序
    return merge(left, right)   # 合并排序后的数组

def merge(left, right):
    result = []   # 合并后的数组
    i = j = 0   # 左右数组的指针
    while i < len(left) and j < len(right):   # 遍历左右数组，直到其中一个数组遍历完
        if left[i] < right[j]:   # 左数组元素小于右数组元素，放入结果数组
            result.append(left[i])
            i += 1
        else:   # 右数组元素小于左数组元素，放入结果数组
            result.append(right[j])
            j += 1
    result += left[i:]   # 左数组剩余元素放入结果数组
    result += right[j:]   # 右数组剩余元素放入结果数组
    return result   # 返回合并后的数组

# 测试
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(merge_sort(arr))   # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]