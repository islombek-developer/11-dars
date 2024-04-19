# class CustomRange:
#     def __init__(self, start, end, step=None):
#         self.current = start
#         self.end = end
#         self.step = step

#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current <= self.end:
#             result = self.current

#             if self.step is None:
#                 self.current+=1
#             else:
#                 self.current+=self.step
#             return result
#         else:
#             raise StopIteration

# for num in CustomRange(4,9):
#     print(num)





# def quicksort(x):
#     if len(x) <= 1:
#         return x
#     else:
#         a = x[0]
#         lesser = [i for i in x[1:] if i <= a]
#         greater = [i for i in x[1:] if i > a]
#         return quicksort(greater) + [a] + quicksort(lesser)

def binary_search(x, target):
    c=0
    if len(x) <= 1:
        return x
    else:
        a = x[0]
        lesser = [i for i in x[1:] if i <= a]
        greater = [i for i in x[1:] if i > a]
        c=binary_search(greater, target) + [a] + binary_search(lesser, target)
    start = 0
    end = len(c) - 1
    while start <= end:
        mid = (start + end) // 2
        mid_value = c[mid]
        if mid_value == target:
            return mid
        elif mid_value > target:
            end = mid - 1
        else:
            start = mid + 1

d = [3, 6, 8, 10, 1, 2, 1]
print(binary_search(d, 2))




# class Iterator:

#     def __init__(self, list_of_numbers):
#         self.current = 0
#         self.end = len(list_of_numbers)-1
#         self.list_of_numbers = list_of_numbers

#     def __iter__(self):
#         return self


#     def __next__(self):
#         if self.current <= self.end:
#             result = self.list_of_numbers[self.current]
#             self.current +=1
#             return result
#         else:
#             raise StopIteration