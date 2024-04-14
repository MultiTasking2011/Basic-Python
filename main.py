# Data Structures
# 1. LIST->[]

# a = [1,2,3,4,'a','defghi']


# if b in a:
#     print()

# print(a[2::4])

# for i in a:
#     print(i, end="\t")

# for i in range(len(a)):
#     print(i, a[i])

# for i, j in enumerate(a):
#     print(i, j)

# Adding items
# a.append("abcdef")
# a.insert(0, "item_1")

# deleting items
# a.pop(2)
# a.remove("defghi")

# print(a)

#2. Disctionaries -> {k:v}


a = {"name": "Suraj", "age": 111}

# print(a["name1"]) #indexing with a key name

# print(a.get("name"))

b = dict()

b["gender"] = []
b["gender"].append("Male")
b["gender"].append("Female")


# print(b)

# .keys(), .values(), .items()

for i,j in a.items():
    print(i,j)

#3. Sets -> {}

c = [1,7,3,5,6,7,3]

print(list(set(c)))

# 4. Tuples -> ()

# Tuples are same as List, just the fact that you cannot add, update or delete items
x = [1,2,3]

print(tuple(x))