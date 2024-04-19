# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
# print(duplicate_encode("(( @"))


# def factorial(max=0):
#     result = 0
#     while result <= max:
#         yield 2 ** result
#         result += 1

# j = factorial(4)


# class Powtwo:
#     def __init__(self,max=0):
#         self.n=0
#         self.max=max

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.n>self.max:
#             raise StopIteration
#         result=2**self.n
#         self.n+=1
#         return result
# numbers=Powtwo(4)
# for i in numbers:
#     print(i)



# def factorial(n):
#     result=1
#     for i in range(1, n+1):
#         result*=i
#         yield result
# for j in factorial(6):
#     print(j)


# def count(son):
#     count=1
#     while count<=son:
#         yield count
#         count+=1

# for i in count(5):
#     print(i)