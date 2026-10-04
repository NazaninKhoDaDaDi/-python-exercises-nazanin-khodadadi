inventory = {
'apple': 20,
'banana': 5,
'orange': 0,
'milk': 12,
'bread': 0
}

available_count = 0
out_count = 0

print('Available:')
for i in inventory:
    if inventory[i] > 0 :
        print(i)
        available_count = available_count + 1

print()

print('Out of stock:')
for i in inventory:
    if inventory[i] == 0 :
        print(i)
        out_count = out_count + 1
        
print()
print('Available_count : ', available_count)
print('Out_count : ', out_count)
