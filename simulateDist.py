#Seed on line Number 6
from random import *
import sys
import math

seed(10)   # Here the value of seed is 10. Change it with any desired value.

# Bernoulli distribution
numOfSamples = int(sys.argv[1])
distribution = sys.argv[2]


if(distribution == "bernoulli"):
    probability = float(sys.argv[3])
    for i in range(numOfSamples):
        randomNumber  =  random()
        if(randomNumber <= probability):
            print "Bernoulli Sample generated: 1"
        else:
            print "Bernoulli Sample generated: 0"

elif(distribution == "binomial"):
    n = int(sys.argv[3])  # Given command line argument "n"
    tempMean  = 0
    probability = float(sys.argv[4])
    for i in range(numOfSamples):
        count = 0
        for j in range(n):
            randomNumber = random()
            if(randomNumber <= probability):
                count = count + 1
        print "Binomial sample is %r"%count
        tempMean+=count
    val = tempMean/numOfSamples
    #print "Temp Mean of the entire samples: %r"%val


elif(distribution == "geometric"):
    probability = float(sys.argv[3])
    tempMean = 0
    for i in range(numOfSamples):
        count = 0
        while True:
            randomNumber = random()
            count = count + 1
            if(randomNumber <= probability):
                break
        print "Geometric sample is %r"%count
        tempMean+=count
    val = tempMean/numOfSamples
    #print "Temp Mean of the entire samples: %r"%val

elif (distribution == "neg-binomial"):
    k = int(sys.argv[3]) # k is the number of successes (as given in pdf)
    probability = float(sys.argv[4])
    tempMean = 0
    for i in range(numOfSamples):
        count = 0
        successCount = 0
        while True:
            randomNumber = random()
            count = count + 1
            if(randomNumber <= probability):
                successCount+=1
            if (successCount==k):
                break
        print "Negative Binomial sample is %r"%count
        tempMean+=count
    val = tempMean/numOfSamples
    #print "Temp Mean of the entire samples: %r"%val


elif (distribution == "poisson"):
    lamda = float(sys.argv[3])
    tempMean = 0
    for it in range(numOfSamples):
        sum = 0
        randomNumber = random()
        j = 0
        while (sum<randomNumber):  # First Formula given by professor i.e., F(x) >= u > F(x-1)
            ePowerMinusLamda = math.exp(-lamda)
            lamdaPowerJ = math.pow(lamda,j)
            jFactorial = math.factorial(j)
            sum = sum + ((ePowerMinusLamda*lamdaPowerJ)/jFactorial)
            j+=1
        print "Poisson sample is %r"%j
        tempMean+=j
    val = tempMean/numOfSamples
    #print "Temp Mean of the entire samples: %r"%val

elif (distribution == "arb-discrete"):
    probabilityList = []
    tempMean  = 0
    for it in range(numOfSamples):
        sum = 0
        randomNumber = random()
        for i in range(3,len(sys.argv)):
            probabilityList.append( float(sys.argv[i]) )
        j = 0
        while (sum<randomNumber):  # First Formula given by professor i.e., F(x) >= u > F(x-1)
            sum+=probabilityList[j]
            j+=1
        print "Arbitary Discrete sample is %r"%j
        tempMean+=j
    val = tempMean/numOfSamples
    #print "Temp Mean of the entire samples: %r"%val



elif (distribution=="uniform"):
    tempMean = 0
    a = float(sys.argv[3])
    b = float(sys.argv[4])
    j = 0
    for i in range(numOfSamples):
        randomNumber = random()
        j = a+randomNumber*(b-a)
        print "Uniform sample is %r"%j
        tempMean+=j
    val = tempMean/numOfSamples
    #print "Temp Mean of the entire samples: %r"%val

elif (distribution == "exponential"):
    tempMean = 0
    j = 0
    lamda = float(sys.argv[3])
    for i in range(numOfSamples):
        randomNumber = random()
        j = -((1/lamda)*math.log(1-randomNumber))
        print "Exponential sample is %r"%j
        tempMean+=j
    val = tempMean/numOfSamples
    #print "Temp Mean of the entire samples: %r"%val


elif (distribution == "gamma"):
    tempMean = 0
    alpha = int(sys.argv[3])
    lamda = float(sys.argv[4])
    for i in range(numOfSamples):
        sum = 0
        for j in range(alpha):
            randomNumber = random()
            sum+= (-((1/lamda)*math.log(1-randomNumber)))
        print "Gamma sample is %r"%sum
        tempMean+=sum
    val = tempMean/numOfSamples
    #print "Temp Mean of the entire samples: %r"%val

elif (distribution == "normal"):
    tempMean = 0
    mean = float(sys.argv[3])
    standardDeviation = float(sys.argv[4])
    num = int(math.floor(numOfSamples/2))
    for i in range(num):
        u1 = random()
        u2 = random()
        z1 = (math.sqrt(-2*math.log(u1)))*math.cos(2*3.14*u2)
        z2 = (math.sqrt(-2*math.log(u1)))*math.sin(2*3.14*u2)
        x1 = mean+standardDeviation*z1
        x2 = mean+standardDeviation*z2
        print "Normal Sample is %r , %r"%(x1,x2)
        tempMean = tempMean+x1+x2

    if(numOfSamples%2!=0):
        u1 = random()
        z1 = (math.sqrt(-2*math.log(u1)))*math.cos(2*3.14*u2)
        x1 = mean+standardDeviation*z1
        print "Normal Sample is %r "%x1
        tempMean = tempMean+x1
    val = tempMean/numOfSamples
    #print "Temp Mean of the entire samples: %r"%val
