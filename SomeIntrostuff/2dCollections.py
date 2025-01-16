fruits=["apple","orange","banana","coco"]
vegetables=["celery","carrots","fries"]
meats=["beef","chicken","turkey"]

groceries= [fruits,vegetables,meats]


print(groceries[1])
print(groceries[0][0])


g2=[["apple","orange","banana","coco"],["celery","carrots","fries"],["beef","chicken","turkey"]]
print(g2[1])
print()
for collection in g2:
    print(collection)
print()

for collection in g2:
    for food in collection:
        print(food,end=" ")
    print()


#keypad ex tuple faster than list

pad=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

for row in pad:
    for num in row:
        print(num, end=" ")
    print()
