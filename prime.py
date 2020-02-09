import numpy as np

def isPrime(x):
    if (x <= 3):
        return True
    elif( x % 2 == 0 or x % 3 == 0):
        return False
    else:
        i = 5
        while(i < x):
            if(x % i == 0):
                return False
            i += 1
        return True

def nFirstPrimes(n):
    answer = np.zeros(n)
    answerCount=0
    limiar=2
    count=0
    while(answerCount < n):
        poss = np.arange(limiar,(n+limiar),1)
        limiar+=n
        for i in poss:
            if(isPrime(i) and count < n):
                answer[count] = i
                answerCount+=1
                count+=1
        
    return answer

# Test
print(nFirstPrimes(100))
