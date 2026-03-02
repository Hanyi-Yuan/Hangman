from random import choice
import json

def word_check(letter='',target=''):#function because I'm lazy, checks for words
    
    result=[]

    for i in range(len(target)):
        if letter in target[i]:
            result.append(i)

    return result

def input_check(temp): #temp=input; chcks if input is valid
    flag=True

    if len(temp)>1: #check lenght
        return False
    
    try:
        int(temp) #check number
        flag=False
    except:
        pass
       
    return flag #returns true if passes check

print("Let's play hangman")

def hangman():

    with open('word_bank.json','r') as word_access: #opening json as obj word_access
        contents=json.load(word_access) #reading

    temp_ls=contents['words'] #in dictionary format
    word_access.close() #closing file

    target_word=choice(temp_ls) #getting random word
    wrong_guesses=set([]) #no repeats

    win=False #because they have not yet won
    display=['_' for i in target_word]#for the _ _ _ _ _ print and tracking
    lives=2*len(target_word)-2 #generous amount of lives for now

    while lives>0: #loop...
        print(f"Guess a letter(lives={lives}):") #prompt for hangman
        print(str(display).replace("'",'').replace('[','').replace(']','').replace(',','')) #str for easy read; why am I so lazy?
        user_input=input().lower() #collcting input and changing to lower case
        if(not input_check(user_input)): #input_check will check for validity of input
            print('Invalid input! Only single length letters are allowed!')
            continue #will repeat loop while disregarding the actions below

        if(user_input in display): #input check for repition
            print('already guessed, please try again.')
            continue

        elif(user_input in wrong_guesses): #input chck for repition

            print('this letter was already guessed. The following letters have already been guessed:')
            temp=list(wrong_guesses) #for iterating

            for k in range(len(temp)-1): #leaves out last element for formating
                print(temp[k],end=',')

            print(temp[-1]) #last element
            continue

        check=word_check(user_input,target_word)#prompts for input, then checks the input
        
        try: #error handling and me being lazy
            for j in check:
                display[j]=user_input #changing tracker

            check.pop(0)# triggers error if empty so it will go into except instead
            print("Correct guess!")

        except:
            print("Wrong!")
            wrong_guesses.add(user_input) #tracking wrong guess

        win=not '_' in display #win=false when there is something needing to be guessed

        if win:#checking win condition
            print(f'You won with {lives} lives remaining!')
            break

        lives-=1 #making sure loop is not infinite

    print("you lost, try again next time."*(not win)) #bool is auto converted to int in operations

hangman() #initial call

while True: #looped call once first call finishes
    if(input('do you want to play again?(y/n)\n')=='y'): #shorthand code to ask the play again prompt and respond
        hangman()
    else:
        break

