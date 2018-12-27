Prime = [2]
ret   = []

def isPrime(num):
    for pri in Prime:
        if num%pri == 0 :
            return False
    return True

def Check(num):
    for pri in Prime:
        if (num - pri) in Prime:
            return False
    return True

def main(num):
    for i in range(3,num + 1):
        if isPrime(i):
            Prime.append(i)
        else:
            if i%2 == 0 :
                if Check(i): ret.append(i)
    
    print(ret)




if __name__=='__main__':
    main(100000)