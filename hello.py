x = "Hello World!"
print(x)
n = 3.14
print(f"Ceci est le nombre pi :{n}");

def add(i,j):
    return i+j

x = add(3,2)
print(x)

i = 0
while i < 10:
    print(i)
    i+=1

for i in range(10):
    if i % 2 == 0:
        print(i)

def isPrime(n):
    res = True
    if n < 2:
        res = False
    else:
        for i in range(2,n):
            if n%i == 0:
                res = False
    return res

print(isPrime(7))
print(isPrime(8))

l = [1,2,3,4,5,6,7,8,9]
#l = range(1,10)
i = 3
x = l[i]
l.append(99)
l.remove(99)
for i in l:
    print(i)

#sum
#min
#max
#average
#getPrimeNumbers
#inverse