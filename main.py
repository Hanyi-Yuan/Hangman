from random import choice
print("Let's play hangman")

word_access=open('word_bank.txt','r') #access previous file
temp_ls=word_access.read() #reading file
word_access.close() #closing file

target_word=choice(temp_ls) #getting random word

print(target_word) #debug more stuff later
