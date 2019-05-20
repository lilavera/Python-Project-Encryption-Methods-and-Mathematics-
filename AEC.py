import matplotlib.pyplot as plt
import numpy as np

import random
import base64
import hashlib
import sys
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

#checking if number is prime for mobius function
def isPrime(n) : 
  
    if (n < 2) : 
        return False
    for i in range(2, n + 1) : 
        if (i * i <= n and n % i == 0) : 
            return False
    return True


def mobius(N) :       
    
    if (N == 1) : 
        return 1
  
    # For a prime factor i  
    # check if i^2 is also 
    # a factor. 
    p = 0
    for i in range(1, N + 1) : 
        if (N % i == 0 and 
                isPrime(i)) : 
  
            # Check if N is 
            # divisible by i^2 
            if (N % (i * i) == 0) : 
                return 0
            else : 
  
                # i occurs only once,  
                # increase f 
                p = p + 1
  
    # All prime factors are 
    # contained only once 
    # Return 1 if p is even 
    # else -1 
    if(p % 2 != 0) : 
        return -1
    else : 
        return 1
    
    
    
#eulerFunction


def gcd(a, b):   
    if (a == 0): 
        return b 
    return gcd(b % a, a) 
  

def phi(n):   
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1): 
            result+=1
    return result 

#plotforulerFunction  
def eulerplot(a):
    eudots=[]
    for i in range(1,a):
        k=phi(i)
        eudots.append(k)
    plt.scatter(range(1,a),eudots,edgecolors='green')
    plt.plot(range(1,a),eudots)
    plt.xticks(np.arange(1,a,step=1))
    plt.yticks(np.arange(1,a,step=1))
    plt.show();
eulerplot(15)    
        
      
    
#plotForMobiusFunction    

def mobplot(t):    
    dots=[] 
    for i in range(0,t):
        a=mobius(i)
        dots.append(a)
    plt.scatter(range(0,t),dots,edgecolors='red')
    #plt.plot(range(0,t),dots)
    plt.xticks(np.arange(0, t, step=1))
    plt.yticks(np.arange(-1, 1.1, step=1))
    plt.show();
mobplot(15)



#DH generators

size=15

def plotDW(p):
    matrix = [[]]
    matrix = [[(i**j)%p for i in range(1,size+1)] for j in range(1,size+1)]
    df_cm = pd.DataFrame(matrix, range(size),
                  range(size))
    plt.figure(figsize = (10,7))
    sn.set(font_scale=1.4)#for label size
    sn.heatmap(df_cm, annot=True,annot_kws={"size": 16})# font size

plotDW(17)



#TO DO:RHS
def RHS():
    p=int(input('Enter prime p: '))
    q=int(input('Enter prime q: '))
    print("Choosen primes:\np=" + str(p) + ", q=" + str(q) + "\n")
    n=p*q
    print("n = p * q = " + str(n) + "\n")
    phi=(p-1)*(q-1)
    print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")
    def gcd(a, b):
        while b != 0:
            c = a % b
            a = b
            b = c
        return a
    def modinv(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None
    def coprimes(a):
        l = []
        for x in range(2, a):
            if gcd(a, x) == 1 and modinv(x,phi) != None:
                l.append(x)
        for x in l:
            if x == modinv(x,phi):
                l.remove(x)
        return l
    print("Choose an e from a below coprimes array:\n")
    print(str(coprimes(phi)) + "\n")
    e=int(input())
    d=modinv(e,phi)
    print("\nYour public key is a pair of numbers (e=" + str(e) + ", n=" + str(n) + ").\n")
    print("Your private key is a pair of numbers (d=" + str(d) + ", n=" + str(n) + ").\n")
   # def encrypt_block(m):
     #   c = modinv(m**e, n)
      #  if c == None: print('No modular multiplicative inverse for block ' + str(m) + '.')
     #   return c
    #def decrypt_block(c):
       # m = modinv(c**d, n)
       # if m == None: print('No modular multiplicative inverse for block ' + str(c) + '.')
       # return m
   # def encrypt_string(s):
       # return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
  #  def decrypt_string(s):
      #  return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
    
    
#all functions
RHS()        




