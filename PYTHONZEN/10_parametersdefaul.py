def find_volume(length, width, depth):
  return length * width * depth

print(find_volume(10,20,30))

def find_volume(length=1, width=1, depth=1):
  return length * width * depth

print(find_volume(width=30))
def find_volume(length=1, width=1, depth=1):
  return length * width * depth, "Hola"

print(find_volume(width=30))

def find_volume(length=1, width=1, depth=1):
  return length * width * depth, width, 'hola'

result, width, text = find_volume(width=10)

print(result,width,text)
