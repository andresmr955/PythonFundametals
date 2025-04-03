items = [
    {
        'product' : 'shirt', 
        'price' : 100,
        
    },
    {
        'product' : 'pants', 
        'price' : 300,
    },
    {
        'product' : 'shoes', 
        'price' : 200,
    },
]


result = list(map(lambda item : item['price']  , items))

print(result)

# We can nnot use lambda because we are going to add a new key to the dictionary
#result = list(map(lambda item : item['price'] * 0.19   , items))
#print(result)


def add_tax(item):
    item['tax'] = item['price'] * 0.19
    return item

result = list(map(add_tax, items))

print(result)

print(items)

##How to change the reference in memory


def add_tax(item):
    new_item = item.copy()
    new_item ['tax'] =  new_item ['price'] * 0.19
    return new_item

result = list(map(add_tax, items))
print(items)
print(result)

