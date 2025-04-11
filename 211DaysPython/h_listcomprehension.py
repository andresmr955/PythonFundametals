user_input = [
  "text", "test", "python", "example"
]



def find_words_with_two_vowels(words):
  # Tu código aquí 👈
    vowels = "aeiouAEIOU"  
    
    solution = [word for word in words if sum(word.count(vowel) for vowel in vowels) == 2]
          
    return solution

print(find_words_with_two_vowels(user_input))