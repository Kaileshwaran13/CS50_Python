deep = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
deep = deep.strip()
deep = deep.lower()
if deep == "42" or deep == "forty-two" or deep == "forty two":
    print("Yes")
else:
    print("No")