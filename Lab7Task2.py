words = []

while True:
    s = input("Введіть строку: ")

    if s == "":
        break
    
    else:
        for word in s.split(" "):
            if word not in words:
                words.append(word)

print(", ".join(words))