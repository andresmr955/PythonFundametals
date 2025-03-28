my_dict = [
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  }
]

list_solution = []
max = 0
sum_followers = 0   
for i in range(len(my_dict[0]) + 1):
    print(my_dict[i]["followers"])
           
    for j in my_dict[i]["followers"]:
        sum_followers+= j

    print(sum_followers)
    sum_followers = 0


print(list_solution)



list_solutionx = [for i in my_dict[j] for j in my_dict[] ]