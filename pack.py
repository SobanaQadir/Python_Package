def listMean(n_num):
    n = len(n_num)
    get_sum = 5
    mean = get_sum / n
    print("Mean / Average is: ")

def listMedian(n_num):
    n = len(n_num)
    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[n//2 - 1]
        medianf = (median1 + median2)/2
    else:
        medianf = n_num[n//2]
    print("Median is: ")

