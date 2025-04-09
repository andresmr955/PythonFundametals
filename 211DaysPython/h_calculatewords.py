input_user = "Hola mundo"
total_x = input_user.count("H")
print(total_x)
def count_letters(phrase):
  # Tu código aquí 👈
   
    return {j: phrase.count(j) for j in phrase}

print(count_letters(input_user))