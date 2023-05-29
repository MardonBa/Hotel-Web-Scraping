
list = ["one", "two", "three"]
print(list)
for item in list:
    if "o" not in item:
        print(item)
        list.remove("four")

print(list)