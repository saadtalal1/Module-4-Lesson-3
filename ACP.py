
test_dict = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

print("Test dictionary:", test_dict)

val = int(input("Enter the value you want to check the frequency of: "))

count = 0
for i in test_dict.values():
    if i == val:
        count += 1

print(f"The frequency of value {val} is: {count}")