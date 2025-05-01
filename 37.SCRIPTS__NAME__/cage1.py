# cage.py

def dog1():
    print("Dog 1 is ready to go for a run!")

def dog2():
    print("Dog 2 is ready to go for a run!")
dog2()

def dog3():
    print("Dog 3 is ready to go for a run!")

# Leash: dog3 only runs if you execute the file directly
if __name__ == "__main__":
    print("This is cage.py and it is being executed directly.")
    dog1()
