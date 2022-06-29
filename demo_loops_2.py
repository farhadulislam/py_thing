for x in "Bangladesh":
    print(f"The  char is {x}")

for x in [0, 1,2,3, 34, 45, 67, 80, 40, 53]:
    if x%10==0:
        print(x)

for x in range(10):
    if x>10:
        break
    print(x+1)

main_dishes = ["Noodles", "Rice", "Biryani", "Parota"]
desserts = ["Doi", "Lassi", "Falooda", "Ice Cream"]

for x in main_dishes:
    for y in desserts:
        print(x, y)

print(f"NUM of DISHES : {len(main_dishes)}")

for x in range(2, 20, 2):
    print(x)


for x in range(100, 110):
    if x%2!=0:
        print(x)


for x in range(301, 340):
    if x == 333:
        break
    print(x)
else:
    print(f"Looped over")


for x in [23, 34, 56, 79]:
    pass


list_numbers = [12, 23, 25, 60.2, 45, 89]
sum = 0

for i in list_numbers:
    sum = sum + i
    print(f"INDEX {list_numbers.index(i)} : NUMBER {i}")

print(sum)



def factorial(x):
    factorial  = 1
    if x ==1:
        return 1
    else:
        for i in range(1, x+1):
            factorial = factorial * i
        return factorial

print(factorial(3))