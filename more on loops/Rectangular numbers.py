'''
Rectangular numbers
Print the following pattern for the given number of rows.
Pattern for N = 4
4444444
4333334
4322234
4321234
4322234
4333334  
4444444
'''
n=int(input())
answer=[['1']]
for i in range(2, n+1):
    #print("i= "+str(i))
    t=[str(i)]*((2*i)-3)
    t2=[str(i)]*((2*i)-3)
    answer.insert(0, t2)
    answer.append(t)
    for a in answer:
        a.insert(0,str(i))
        a.append(str(i))

answerfinal=[]
for a in answer:
    answerfinal.append("".join(a))
for a in answerfinal:
    print(a)