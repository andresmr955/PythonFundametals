to_do = ["go to the hotel",
         "go to lunch",
         "go to museum",
         "come back to hotel"]
print(to_do)
numbers = [1,2,3,4, "cinco"]
print(type(numbers))
mix = ['uno', 2, 3.14, True, [1,2,3] ]

#length
print(len(mix))
print("First element ", mix[0])
print("Second element ", mix[1])
print("Last element ", mix[-1])

#slicing
string = "Hola Mundo"
print("First element ", string[0])
print("Slicing mix from 0 to 2", mix[0:2])
print("Slicing mix from 2 to the end", mix[2:])
print("Slicing from the end to 2: ", mix[:2])

#append
print(mix)
mix.append(False)
print("Appending ", mix)
print(mix)
mix.append(["a", "b"])
print(mix)