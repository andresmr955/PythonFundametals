sets_user = [
  {1, 2, 3, 4},
  {2, 3, 4, 5},
  {3, 4, 5, 6}
]

def find_set_intersection(sets):
  # Tu código aquí 👈
    
    if len(sets) == 0:
        return set()
    return sets[0].intersection(*sets[1:])

print(find_set_intersection(sets_user))