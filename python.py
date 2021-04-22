def standard_div(arr):
    # find the mean
mean = statistics.mean(arr)
sum = 0
    # iterate over the array
for i in arr;
        # subtract each number - mean
        dif = i - mean
        # square it
        dif_sq = dif**2
        # add to the sum
        sum+= dif_sq

    # divide the sum by the number of elements in the array
    variance = sum / count (arr)
    # take the square root
std = math.sqrt(variance)
    # return standard deviation
    return std
    
