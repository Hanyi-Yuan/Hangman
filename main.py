from random import choice

def word_check(letter='',target=''):#function because I'm lazy
    result=[]
    for i in range(len(target)):
        if letter in target[i]:
            result.append(i)

    return result

def input_check(temp):#temp=input
    flag=True
    if len(temp)>1: #check lenght
        return False
    try:
        int(temp) #check number
        flag=False
    except:
        pass
       
    return flag

print("Let's play hangman")

def hangman():
    word_access=open('word_bank.txt','r') #access previous file
    temp_ls=word_access.read() #reading file
    temp_ls=['hello','testing']#temporary testing
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
        if(not input_check(user_input)):
            print('Invalid input! Only single length letters are allowed!')
            continue
        check=word_check(user_input,target_word)#prompts for input, then checks the input
        
        try:#error handling and me being lazy
            for j in check:
                display[j]=user_input
            check.pop(0)# triggers error if empty
            print("Correct guess!")
        except:
            print("Wrong!")

        win=not '_' in display

        if win:
            print(f'You won with {lives} lives remaining!')
            break
        else:
            print(f"wrong guesses:{wrong_guesses}")
        lives-=1

    print("you lost, try again next time."*(not win))

while True:
    hangman()
    if(input('do you want to play again?(y/n)\n')=='y'):
        hangman()
    break
