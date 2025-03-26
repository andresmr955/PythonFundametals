## Read a file line by line

'''
with open('tale.txt', 'r') as file:
    for line in file:
        ##remove any leading and trailing whitespace 
        print(line.strip())


'''

## Read all lines in a list

'''
with open('tale.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
'''

## Add texto to the file
'''
with open('tale.txt', 'a') as file:
    file.write("\n\nBy: Andres")
'''

##Overwrite the file
'''

with open('tale_overwrite.txt', 'w')as file:
    file.write("\n\n This document was deleted and now I am the real text")

'''

##CHALLANGE
'''

with open('tale.txt', 'r' ) as file:
    content = file.readlines()
    print(f'The total lines in the file tale.txt are {len(content)}')

'''

##CHALLANGE DIFFICULT

with open('tale.txt', 'r') as file:
        ## Here we have to read it obligated
        content = file.read()
        ##using split
        content_n = content.split('\n')
        print(f'The total lines in this file are {len(content_n)} lines')