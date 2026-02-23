from random import choice

def word_check(letter=''): #function that returns a list of all coincidences of the letter
    result=[]
    for i in range(len(target_word)):
        if letter in target_word[i]:
            result.append(i)

    return result

print("Let's play hangman")

word_access=open('word_bank.txt','r') #access previous file
temp_ls=word_access.read() #reading file
word_access.close() #closing file

target_word=choice(temp_ls) #getting random word
wrong_guesses=[]

print(target_word) #debug

win=False
display=['_' for i in target_word]#for the _____ print
lives=2*len(target_word)-2 
while lives>0:
    print(str(display)) #str for easy read
    user_input=input(f"Guess a letter(lives={lives}):\n")
    check=word_check(user_input)#prompts for input, then checks the input

    try:#error handling and me being lazy
        for j in check:
            display[j]=user_input
        check.pop(0)# triggers error if empty
        print("Correct guess!")
    except:
        print("Wrong!")

    win=not '_' in display #when its filled

    if win: #checking win conditions
        print(f'You won with {lives} lives remaining!')
        break
    else:
        print(f"wrong guesses:{wrong_guesses}")
    lives-=1

print("you lost, try again next time."*(not win))#only prints when win=False
