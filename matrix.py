from random import randint

row = 3
col = 3
x = []

for i in range(row):
    y = []
   
    for j in range(col):
        y.append(randint(1,100))
    x.append(y)
    
for i in x:
    for j in i:
        print("%3d" %j,end = ' ')#%3d due to generating gap between row & column
    print()

## output:
## 48  88  93 
## 30  81  35 
## 26  90  47 
