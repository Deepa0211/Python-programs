sentence = "how are you?".split()

print(sentence)

list = []

for i in sentence:
    print(i.capitalize())
    list.append(i.capitalize())

print(list)

print(" ".join(list))
    