print("値の入力")
n = int(input())

i = 2

print_primefactor = []

while(n>=i):
    if(n%i == 0):
        n = n/i
        print_primefactor.append(i)
    else:
        i += 1

print(print_primefactor)