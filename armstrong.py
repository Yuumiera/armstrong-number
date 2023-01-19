# armstrong-number
def armstrong_finder(upper_limit):

    for i in range(upper_limit):
        a = len(str(i))
        p = 0
        for j in str(i):
            p += pow(int(j),a)
            if p == i:
                print(i)

upper_limit=9999
armstrong_finder(upper_limit)
