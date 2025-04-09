user_words = ["racecar", "level", "world", "hello"]
non_pali = ["Platzi", "Python", "django", "flask"]
#print(user_words[0][0])
#print(user_words[0][0:])
#print(user_words[0][0:3])
#print(user_words[4][::-1])

def find_largest_palindrome(words):
  # Tu código aquí 👈
    biggest = ""
    for word in words:
        if word == word[::-1] and len(word) > len(biggest):
            biggest = word   
            
    return biggest if biggest else None

print(find_largest_palindrome(non_pali))