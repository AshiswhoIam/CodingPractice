for x in range(1,4):
    print(x)
print("normal count")

for y in range(1,7,2):
    print(y)
print("timer done")

number="1234-3243-4234-6454"

for z in number:
    print(z)
print("number  done")

for a in range(1,5):
    if a == 2:
        continue
    else:
        print(a)
print("cont  done")

for b in range(1,5):
    if b== 2:
        break
    else:
        print(b)

rows= int(input("enter # of rows: "))
col= int(input("enter # of col: "))
symbol= input("enter a symbol: ")

for z in range(rows):
    for p in range (col):
        print(symbol, end=" ")
    print()



