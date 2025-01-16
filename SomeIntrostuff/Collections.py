#list []-> order and change dupok  set {}-> undordder no change add/rem ok tuple ()->rdered unchange dup ok

fruit =["apple","orange","banana","mango"]

print(fruit[1])
print(fruit[0:3])
print(fruit[::2])
print(fruit[::-1])

for f in fruit:
    print(f)

#print(dir(fruit))
#print(help(fruit))
print(len(fruit))
print("apple" in fruit)
print("coco" in fruit)

fruit[0]="coco"
for f in fruit:
    print(f)

fruit.append("lychee")

for f in fruit:
    print(f)

fruit.remove("orange")

print(fruit)

fruit.insert(0,"pomme")
print(fruit)
fruit.sort()
print(fruit)
fruit.reverse()
print(fruit)
#fruit.clear
print(fruit.index("mango"))
print(fruit.count("mango"))


fruits ={"apple","orange","banana","mango","mango"}
fruits.add("coco")
#fruits.remove("coco")
#fruits.pop()
print(fruits)

fruitss =("apple","orange","banana","mango","mango")
print(fruitss.index("apple"))
print(fruitss.count("mango"))
for f in fruitss:
    print(f)


#small ex

foods = []
prices=[]
total= 0


while True:
    food=input("enter a grocery to purchase or q to quit: ")
    if food.lower() =="q":
        break
    else:
        price= float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("---- Cart ----")
for food in foods:\
    print(food, end=" ")

for price in prices:
    total+= price
print()
print(f"Your total is : ${total}")