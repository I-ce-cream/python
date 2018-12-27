Prime = [2,3,5,7]
ret   = []

def isPrime(num):
    for pri in Prime:
        if num%pri == 0 :return False
    return True

def Check(num):
    for i,pri in enumerate(Prime):
        if (num - pri) in Prime: return False
        if pri > (num/2) : return False
    return True

def main(num):
    for i in range(10,num + 1):
        if isPrime(i):
            Prime.append(i)
        else:
            if i%2 == 0 :
                if Check(i): ret.append(i)
    
    print(ret)




if __name__=='__main__':
    main(10000)