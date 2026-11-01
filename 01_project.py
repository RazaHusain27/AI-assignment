'''
s=-1
w=0
g=1
'''
print("choose (-1) for snake ,"
" (1) for gun ,"
"and (0) for water")

you= int(input("enter your choice: "))
print(you)
import random
computer=random.choice([-1, 0, 1])
print(computer)
if computer == you:
    print("you both choose same\nit's draw")
else:
    if computer== -1 and you== 0:
        print("you choose water but computer choose snake\nyou loose")
    elif computer== -1 and you== 1:
        print("you choose gun but computer choose snake\nyou won")
    elif computer== 0 and you== -1:
        print("you choose snake but computer choose water\nyou won")
    elif computer== 0 and you== 1:
        print("you choose gun but computer choose water\nyou loose")
    elif computer== 1 and you== 0:
        print("you choose water but computer choose gun\nyou won")
    elif computer== 1 and you== -1:
        print("you choose snake but computer choose gun\nyou loose")
    else:
        print("something went wrong")





    