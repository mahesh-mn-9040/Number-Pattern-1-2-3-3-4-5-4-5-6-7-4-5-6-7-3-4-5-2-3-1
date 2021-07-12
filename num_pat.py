#1
#2*3
#3*4*5
#4*5*6*7
#4*5*6*7
#3*4*5
#2*3
#1

n=int(input())
st=""
for i in range(1,n+1):
    k=i
    for j in range(1,i+1):
        st=st+str(k)+"*"
        k=k+1
    print(st[:-1])  
    st=""
for i in range(n,0,-1):
    k=i
    for j in range(i+1,1,-1):
        st=st+str(k)+"*"
        k=k+1
    print(st[:-1])  
    st=""   
