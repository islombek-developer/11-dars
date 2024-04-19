

numbers = [3, 7, 24, 28, 33, 39, 70, 78, 78, 84, 103, 107, 111, 134, 135, 138, 150, 164, 176, 178, 186, 189, 193, 226,
           229, 232, 246, 274, 278, 285, 292, 292, 296, 309, 328, 349, 353, 355, 383, 392, 399, 434, 436, 437, 439, 468,
           468, 470, 481, 506, 506, 509, 511, 519, 527, 531, 538, 542, 555, 563, 592, 623, 650, 666, 667, 680, 724, 735,
           736, 740, 754, 768, 771, 807, 821, 842, 845, 849, 853, 858, 872, 875,
           883, 888, 907, 917, 920, 924, 927, 928, 930, 947, 950, 953, 953, 965, 970, 990, 995, 998]

def binary_search(target, sorted_list):
    start = 0
    end = len(sorted_list)-1

    count = 0


    while start <=end:
        mid = (start + end) // 2
        mid_value = sorted_list[mid]

        count+=1

        print(count)
        if mid_value == target:
            return mid
        elif mid_value < target:
            start = mid + 1

        elif mid_value > target:
            end = mid -1



    return "Bu son ro'yhat ichida mavjud emas"


print(binary_search(998, numbers))