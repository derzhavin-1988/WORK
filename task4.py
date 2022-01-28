import statistics
import math
a = list(map(int, input().split(" ")))
b = statistics.median(a)
b = round(b)
count = 0
for id, i in enumerate(a):
    while i!=b:
        if i<b:
            i+=1
            count+=1
        elif i>b:
            i-=1
            count-=1
        else:
            a[id] = i
print(sum(abs(z-b) for z in a))


