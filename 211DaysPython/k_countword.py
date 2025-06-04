user_input = [
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
]

def count_words_by_length(words):
  # Tu código aquí 👈
    #alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    return {length: sum(1 for word in words if len(word) == length) for length in {len(word) for word in words}}    
print(count_words_by_length(user_input))