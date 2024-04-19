
def insertion_sort(nums_list):
    count = 0
    for i in range(1,len(nums_list)):
        key = nums_list[i]
        j = i-1


        while j>=0 and key < nums_list[j]:
            nums_list[j+1] = nums_list[j]
            j-=1
            count+=1

        count+=1
        nums_list[j+1] = key

    return nums_list, count


numbers = [8,5,5,3,2,1]

print(insertion_sort(numbers))