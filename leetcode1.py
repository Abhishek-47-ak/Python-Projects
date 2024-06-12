#Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#Insert Delete Replace
#alphabet=['a','b','c','d','e','f','g','h','j','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
w1arr=[]
w2arr=[]

def replace(w1arr,w2arr,count):
    for i in range(len(w1arr)):
        if w1arr[i]!=w2arr[i]:
            w2arr[i]=w1arr[i]
            count+=1
    print(count)

def add(w1arr,w2arr,count):
    for i in range(len(w1arr)+1,len(w2arr)):
        w1arr.append(w2arr[i])
        count+=1
    replace(w1arr,w2arr,count)
    
def dele(w1arr,w2arr,count):
    for i in w1arr:
        if i not in w2arr:
            w1arr.remove(i)
            count+=1
    replace(w1arr,w2arr,count)
    


def wordconvert(w1,w2):
    count=0
    for i in w1:
        w1arr.append(i)
    for j in w2:
        w2arr.append(j)
    if len(w1)==len(w2):
        replace(w1arr,w2arr,count)
    elif len(w1)>len(w2):
        dele(w1arr,w2arr,count)
    else:
        add(w1arr,w2arr,count)



wordconvert("grey","tracey")        