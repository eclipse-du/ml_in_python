import operator

data =[]
with open('rawdata_ds.txt') as f:
    s = [[float(x) for x in line.strip('\n').split(',')] for line in f]
    
s.sort(key=lambda x:x[0]) 
for (a,b) in s:
    print a,b