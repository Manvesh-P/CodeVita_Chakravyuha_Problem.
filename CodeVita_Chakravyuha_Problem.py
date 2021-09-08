N = int(input("Enter the lenghth:"))

list1 = []

for i in range(0, N):
    temp = []
    for j in range(0, N):
        temp.append(0)
    list1.append(temp)
    
rs = 0
re = N-1
cs = 0
ce = N-1

tot = 1

x_cor = [0]
y_cor = [0]

num = 1

while rs <= re and cs <= ce:
    
    for i in range(cs, ce+1):
        list1[rs][i] = num
        
        if num % 11 == 0:
            tot += 1
            x_cor.append(rs)
            y_cor.append(i)
            
        num += 1
        
    rs += 1
    
    for i in range(rs, re+1):
        list1[i][ce] = num
        
        if num % 11 == 0:
            tot += 1
            x_cor.append(i)
            y_cor.append(ce)
            
        num += 1
        
    ce -= 1
    
    if rs <= re:
        
        for i in range(ce, cs-1, -1):
            list1[re][i] = num
            
            if num % 11 == 0:
                tot += 1
                x_cor.append(re)
                y_cor.append(i)
                
            num += 1
            
        re -= 1
        
    if cs <= ce:
        
        for i in range(re, rs-1, -1):
            list1[i][cs] = num
            if num % 11 == 0:
                tot += 1
                x_cor.append(i)
                y_cor.append(cs)
                
            num += 1
            
        cs += 1
        
        
        
for i in list1:
    for j in i:
        print(j, end=' ')
    print()
    
print("\nTotal Power Points:",tot)

for i in range(0, len(x_cor)):
    print("\n" + "(" + str(x_cor[i]) + "," + str(y_cor[i]) + ")")
