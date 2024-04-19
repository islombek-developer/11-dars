class CustomRange:
    def __init__(self, start, end, step=None):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            result = self.current

            if self.step is None:
                self.current+=1
            else:
                self.current+=self.step
            return result
        else:
            raise StopIteration


for num in CustomRange(4,9):
    print(num)









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