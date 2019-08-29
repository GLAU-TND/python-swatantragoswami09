n=int(input())
#2 54 67 8 5 5 4
# arr=input().split() #['2','54' ,'67' ,'5' ,'5' ,'4']
res=list(map(int ,input().split()))#map(function,)
print(max([res.count(i) for i in res]))