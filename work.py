



nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,19,22,28,33,45,88]

def binary_search(target, numbers):
    start = 0
    end = len(numbers)-1


    while start <=end:
        mid = (start + end) // 2
        mid_value = numbers[mid]

        if mid_value == target:
            return mid

        elif mid_value < target:
            start = mid + 1

        elif mid_value > target:
            end = mid - 1

    return None


nums[binary_search(4, nums)], nums[-1] = nums[-1],nums[binary_search(4, nums)]
nums.pop()
print(nums)
