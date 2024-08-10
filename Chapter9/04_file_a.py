str = "my name is lakhan"

f = open("myFile.txt", "a")
text = f.write(str)
print(text)
f.close()