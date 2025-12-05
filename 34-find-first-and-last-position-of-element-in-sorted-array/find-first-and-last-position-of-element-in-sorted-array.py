def binary_search_first(arr, target):
    left, right = 0, len(arr) - 1
    first=-1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target :
            first=mid
            right=mid-1

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first  # pas trouvé
def binary_search_last(arr, target):
    left, right = 0, len(arr) - 1
    last=-1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target :
            last=mid
            left=mid+1

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last  # pas trouvé
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [binary_search_first(nums,target),binary_search_last(nums,target)]

   
        