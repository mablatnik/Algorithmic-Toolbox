import sys

def optimal_weight(W, w):
    # write your code here
    item =  [0]
    item += list(filter(lambda x : x<=W,w))
    weights = [[0]*(len(item)) for _ in range(W+1)]
    for j in range(1,len(item)):
        for i in range(1,W+1):
            p = weights[i][j-1]
            c = item[j]+weights[i-item[j]][j-1]
            weights[i][j] = p if c>i else max(p,c)
    return weights[-1][-1]
   
if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
