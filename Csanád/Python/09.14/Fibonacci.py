#Fibonacci
fibo = [0,1]

elem = int(input("hanyadik elemet keressük: "))
for i in range(elem-1):
    aktual = fibo[-1]+fibo[-2]
    fibo.append(aktual)
    
print(aktual)