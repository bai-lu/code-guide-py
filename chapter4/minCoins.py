import sys
def minCoins(arr,aim):
    if arr==None or len(arr)==0 or aim<0:
        return -1
    n=len(arr)
    max=sys.maxint
    dp=[[] for x in range(aim+1)]


