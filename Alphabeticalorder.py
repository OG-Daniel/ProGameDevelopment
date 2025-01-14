user_sentence = input("Enter a sentence: ")

us1 = [word.lower() for word in user_sentence.split()]

print(us1)

us1.sort()
print("The sorted words are:")
for word in us1:
   print(word)

