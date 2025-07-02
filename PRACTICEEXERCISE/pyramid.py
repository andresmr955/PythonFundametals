counter = 8
character ="%"
myrows = []


def spacesPyramid(sumatoria,  counterPara):
        return " " * (counterPara - sumatoria) + character * (2 * sumatoria - 1) + " " * (counterPara - sumatoria)



for i in range(counter):    
      myrows.append(spacesPyramid(i + 1, counter))
      
result = ""
for line in myrows:
    result = result + line + '\n'

print(result)