import random
top =input("Type a number:")

if top.isdigit():
  top=int(top)

  if top<=0:
    print('please type a large numberthan 0 next time')
    quit()
else:
    print('please type a number next time.')
    quit()

random_num =random.randint(0,top)
guesses=0

while True:
    guesses+=1
    user_guess=input('make a guess:')
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('please type a number next time.')
        continue

    if user_guess==random_num:
        print('you got it!')
        break
    elif user_guess> random_num:
        print('you were above the number!')
    else:
        print('you were below the number!')

print('you got it in', guesses,"guesses")

