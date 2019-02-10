def mean_num_friends(x):
    sum = 0
    for i in x:
        sum += i
    #print(sum);
    return sum / len(x)


def median_num_friends(x):
    list = sorted(x)
    mid = int(len(x) / 2)
    #if the length of the list is odd, the median is the middle number
    #if the length of the list is even, the median is the mean of the middle two values
    if len(x) % 2 == 0:
        return (list[mid] + list[mid + 1]) / 2
    else:
        return list[mid]


num_friends = [100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean={}".format(mean_num_friends(num_friends)))

print("median={}".format(median_num_friends(num_friends)))