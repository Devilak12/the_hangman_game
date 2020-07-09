from random_word import RandomWords
import string

print('Starting a game of hangman')
f = 0
inattept = 0
while (f == 0):
    inattept = int(input('How Many incorrect attempts do yoy want?'))
    if (inattept > 0 and inattept < 25):
        f = 1
    else:
        print(inattept, " is not between 1 to 25")
minl = int(input('enter minimum lengt of the word'))
m = RandomWords()
r = m.get_random_word(minLength=minl, maxLength=minl)
s = ''
v = []
count = 0
while (inattept > 0 or count == minl):
    i = 0
    print('word:', end=' ')
    while i < minl:
        if i in v:
            print(r[i], end='')
        else:
            print('*', end='')
        i += 1

    print('\nattempt remaining :', inattept)
    print('previous attempt:', s)
    s = input('enter your choice:')
    i = minl - 1
    f = r.find(s)
    if f == -1:
        print(s, " is not in the word")
        inattept = inattept - 1
    else:
        w = s
        v.append(f)
        count = count + 1
    f = 0
if inattept == 0:
    print('game over!!')
else:
    print("YOU WON!!")
