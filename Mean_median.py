def Mean(n_num):
    n = len(n_num)
    get_sum = sum(n_num)
    mean = get_sum / n
    print("Mean / Average is: " + str(mean))

def Median(n_num):
    n = len(n_num)
    n_num.sort()
  
    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = n_num[n//2]
    print("Median is: " + str(median))

