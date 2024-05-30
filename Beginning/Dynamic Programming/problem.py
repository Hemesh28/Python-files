def findprofit(weight,profit,s,n,totalweight):
    if n==0:
        return 0
    if totalweight==0:
        return 0
    if weight[n-1]>totalweight:
        return findprofit(weight,profit,s,n-1,totalweight)
    else:
        return max(findprofit(weight,s+profit[n-1],s,n-1,totalweight-weight[n-1]),findprofit(weight,profit,s,n-1,totalweight))
weight=[4,5,6]
profit=[1,2,3]
n=3
s=0
totalweight=4

print(findprofit(weight,profit,s,n,totalweight))