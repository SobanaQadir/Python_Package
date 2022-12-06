def listMean(n_num):
    n = len(n_num)
    get_sum = sum(n_num)
    mean = get_sum / n
    print("Mean / Average is: " + str(mean))

def listMedian(n_num):
    n = len(n_num)
    n_num.sort()
  
    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[n//2 - 1]
        medianf = (median1 + median2)/2
    else:
        medianf = n_num[n//2]
    print("Median is: " + str(medianf))

