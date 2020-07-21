#Uses python3
import sys
import math


def dist(p1, p2): 
    return float(math.sqrt((p1[0]- p2[0]) * (p1[0] - p2[0]) +(p1[1] - p2[1]) * (p1[1] - p2[1])) )

def bruteForce(P, n): 
    min_val = float('inf')  
    for i in range(n): 
        for j in range(i + 1, n): 
            if dist(P[i], P[j]) < min_val: 
                min_val = dist(P[i], P[j]) 
  
    return min_val 
    
def stripClosest(strip, size, d): 
      
    # Initialize the minimum distance as d  
    min_val = d  
  
    strip.sort(key = lambda p:p[1])
    i=0
    for x,y in strip: 
        j = i + 1
        while j < size and (strip [j][1] - strip[i][1]) < min_val: 
            min_val = dist(strip[i], strip[j]) 
            j += 1
        i+=1
    return min_val
    
def closestUtil(X,Y):
    P=zip(X,Y)
    P=sorted(P)
    Y=[y for _, y in P]
    X=sorted(X)
    n=len(X)
    if n <= 3:  
        return bruteForce(P,len(P))
    mid = n // 2
    midPoint = P[mid]
    dl = closestUtil(X[:mid], Y[:mid]) 
    dr = closestUtil(X[mid:], Y[mid:]) 
    d = min(dl, dr)
    strip=[]
    for i in range(n):  
        if abs(X[i] - X[mid]) < d:  
            strip.append((X[i],Y[i])) 
    return min(d, stripClosest(strip, len(strip), d))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(closestUtil(x, y)))
