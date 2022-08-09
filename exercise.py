list = "list"
print(f"EXERCISES {list}")

ctg_upazilla = ['Hathazari', 'Chandanaish', 'Fatikchhari', 'Raozan', 'Mirsarai', 'Rangunia', 'Panchlaish', 'Satkania', 'Patia', 'Lohagora']
ctg_upazilla.sort()

for upazilla in ctg_upazilla:
    print(f"Chiitagong Upazilla is : {ctg_upazilla.index(upazilla)+1} {upazilla}")

#Start at the beginning but stop before 4th element hence it is 3 (index) in the expr
print(ctg_upazilla[:3])
#Start at the 4th element and all the way till end.
print(ctg_upazilla[3:])
#print all items but in reverse order
print(ctg_upazilla[::-1])
def prob_sol_52():
    for i in range (1000, -1, -1):
        print(i)
        print("\t")
        if i%5==0:
            print("\n")
