import random


def gameWin(comp, you):
 
    if comp == you:
        return None

  
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    
 
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
  
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("Computer Has Chosen.. Waiting For You")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("GG Man You Won The Game!")
else:
    print("Fucking Noob! Get Good, You Lost!! KURWA!! FUCKING MONKE")