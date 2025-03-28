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

def find_famous_cat(cats):
    list_solution = []
    max_seguidores = -1
    cont_followers = 0 

    #This is going to  to print every cat 
    for cat in cats:
      #  print(len(cat["followers"]))
        contador = 0
        cont_followers = 0
        while contador <= len(cat["followers"]):
              for follow in cat["followers"]:
                  cont_followers+= follow
                  contador+= 1
            # print(cont_followers)

              if cont_followers == max_seguidores:
                  list_solution.append(cat["name"])

              elif cont_followers > max_seguidores:
                  max_seguidores = cont_followers
                  list_solution.clear()
                  list_solution.append(cat["name"]) 

            # print(max_seguidores)
              break
        
    return print(list_solution)   
            
find_famous_cat(my_dict)