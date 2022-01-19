def mean_numbers (*args):
    sum_numbers=0
    mean=0
    for i in args:
        sum_numbers += i
        mean=sum_numbers / len(args)
    return mean

print (mean_numbers(1,2,3,4,5,6,7,105))