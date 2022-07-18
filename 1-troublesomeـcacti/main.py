input1 = input()
input2 = input()

n = int(input1)
a = input2.split(' ') 
for i in range(n):
    output = '*' 
    if int(a[i]) <= 3 :
        for j in range(int(a[i])-1):
            output = output + '*'
    print (output)
