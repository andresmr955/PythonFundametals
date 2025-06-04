list1 = [[" " , " " , " " , " ", " "],
         [" " , " " , " " , " ", " "]
         ]
print(len(list1[0]))


column_cust = int(input("Ingresa el numero: "))
column_cust2 = int(input("Ingresa el 2 numero: "))

if list1[column_cust][column_cust2] == " ":
    for i in range(len(list1)):
        for x in range(len(list1[i])):
            list1[i][x] = "S"
           

print(list1)