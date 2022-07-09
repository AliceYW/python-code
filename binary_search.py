# def search_min_diff_element(arr, key):
#     start = 0
#     end = len(arr) - 1
#     i = 0
#     n = len(arr) - 1
#     while start <= end:
#         mid = start + (end - start) // 2
#         if key > arr[mid]:
#             start = mid + 1
#         elif key < arr[mid]:
#             end = mid - 1
#         else:
#             return arr[mid]
#     if (arr[start] - key) < (key - arr[end]):
#         return arr[start]
#     return arr[end]
# print(search_min_diff_element([4, 6, 10], 7))
def find_first_missing_positive(nums):
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1
print(find_first_missing_positive([-3,1,5,4,2]))
