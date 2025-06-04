with open('./text.txt', mode="r+") as file:
    for line in file:
        print(line)
    file.write("write text\n") 

with open('./text.txt', mode="w+") as file:
    for line in file:
        print(line)
    file.write("write new text\n") 
    file.write("write new text\n") 
    file.write("write new text\n") 
